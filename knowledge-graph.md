---
layout: default
title: 知识图谱
permalink: /knowledge-graph/
---

<div class="knowledge-graph-toolbar">
  <input id="knowledge-graph-search" type="text" placeholder="搜索文章、分类、标签或概念" />
  <button id="knowledge-graph-reset" type="button" aria-label="重置视图" title="重置视图">
    <i class="fas fa-rotate-left"></i>
  </button>
</div>

<div class="knowledge-graph-layout">
  <div id="knowledge-graph" class="knowledge-graph-container"></div>
</div>

<style>
  .knowledge-graph-intro {
    background: #f8f9fb;
    border: 1px solid #e5e7eb;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
  }
  .knowledge-graph-toolbar {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 1rem;
    align-items: center;
    flex-wrap: wrap;
  }
  .knowledge-graph-toolbar input {
    flex: 1;
    min-width: 220px;
    padding: 0.6rem 0.8rem;
    border: 1px solid #d0d7de;
    border-radius: 999px;
    font-size: 14px;
  }
  .knowledge-graph-toolbar input:focus {
    outline: none;
    border-color: #8E44AD;
    box-shadow: 0 0 0 3px rgba(142, 68, 173, 0.15);
  }
  .knowledge-graph-toolbar button {
    border: 1px solid #d0d7de;
    background: #fff;
    border-radius: 999px;
    padding: 0.6rem 0.9rem;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
    font-size: 14px;
  }
  .knowledge-graph-toolbar button:hover {
    background: #f0f0f0;
  }
  .knowledge-graph-layout {
    display: block;
  }
  .knowledge-graph-container {
    width: 100%;
    min-height: 88vh;
    border: 1px solid #e5e7eb;
    border-radius: 1rem;
    background-color: #ffffff;
  }
  @media (max-width: 900px) {
    .knowledge-graph-container {
      min-height: 78vh;
    }
  }
  .knowledge-graph-container .echarts-legend {
    background: rgba(255,255,255,0.9);
    padding: 6px 12px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  }
</style>

<script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>

<script>
  document.addEventListener('DOMContentLoaded', function() {

    // ============================================================
    // 1. 定义核心概念及其关系（语义网络骨架）
    //    同时注入现代、专业的配色（Economist 风格参考）
    // ============================================================

const PALETTE = {
  core: '#CC3333',        // 深红（核心概念）
  secondary: '#FF8C42',   // 暖橙（次级概念）
  philosopher: '#003366', // 深海军蓝（哲学家）
  eastern: '#0ABAB5',     // 青绿色（东方思想）
  case: '#2E8B57',        // 海绿色（案例）
  article: '#6B5B95',     // 暗紫（文章）
  category: '#B9770E',    // 金棕（分类）
  tag: '#2B7BB9',         // 专业蓝（标签）
  section: '#1F8A70',     // 节点章节色
  default: '#7C7C7C'      // 中性灰（默认）
};

const CONCEPT_DEFINITIONS = [

  // =================================================================
  // 1. 核心概念（红色 #C0392B）—— 漩涡理论的基石
  // =================================================================
  { id: 'concept:关系', name: '关系', category: '核心概念', color: '#C0392B' },
  { id: 'concept:信息', name: '信息', category: '核心概念', color: '#C0392B' },
  { id: 'concept:生成', name: '生成', category: '核心概念', color: '#C0392B' },
  { id: 'concept:漩涡', name: '漩涡', category: '核心概念', color: '#C0392B' },
  { id: 'concept:动态平衡', name: '动态平衡', category: '核心概念', color: '#C0392B' },
  { id: 'concept:关系第一性', name: '关系第一性', category: '核心概念', color: '#C0392B' },
  { id: 'concept:自指', name: '自指', category: '核心概念', color: '#C0392B' },
  { id: 'concept:涌现', name: '涌现', category: '核心概念', color: '#C0392B' },
  { id: 'concept:僵化', name: '僵化', category: '核心概念', color: '#C0392B' },
  { id: 'concept:韧性', name: '韧性', category: '核心概念', color: '#C0392B' },
  { id: 'concept:河床', name: '河床', category: '核心概念', color: '#C0392B' },
  { id: 'concept:选择性张力', name: '选择性张力', category: '核心概念', color: '#C0392B' },

  // =================================================================
  // 2. 次级概念：系统科学与物理隐喻（橙色 #E67E22）
  // =================================================================
  { id: 'concept:实体', name: '实体', category: '次级概念', color: '#E67E22' },
  { id: 'concept:实体论', name: '实体论', category: '次级概念', color: '#E67E22' },
  { id: 'concept:二元论', name: '二元论', category: '次级概念', color: '#E67E22' },
  { id: 'concept:逻辑类型', name: '逻辑类型', category: '次级概念', color: '#E67E22' },
  { id: 'concept:量子场', name: '量子场', category: '次级概念', color: '#E67E22' },
  { id: 'concept:协变量子场', name: '协变量子场', category: '次级概念', color: '#E67E22' },
  { id: 'concept:量子纠缠', name: '量子纠缠', category: '次级概念', color: '#E67E22' },
  { id: 'concept:贝纳德对流', name: '贝纳德对流', category: '次级概念', color: '#E67E22' },
  { id: 'concept:对称性破缺', name: '对称性破缺', category: '次级概念', color: '#E67E22' },
  { id: 'concept:黏菌', name: '黏菌', category: '次级概念', color: '#E67E22' },
  { id: 'concept:耗散结构', name: '耗散结构', category: '次级概念', color: '#E67E22' },
  { id: 'concept:非平衡态', name: '非平衡态', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自组织', name: '自组织', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自创生', name: '自创生', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自由能原理', name: '自由能原理', category: '次级概念', color: '#E67E22' },
  { id: 'concept:沃尔泰拉方程', name: '沃尔泰拉方程', category: '次级概念', color: '#E67E22' },
  { id: 'concept:怪圈', name: '怪圈', category: '次级概念', color: '#E67E22' },
  { id: 'concept:认知', name: '认知', category: '次级概念', color: '#E67E22' },
  { id: 'concept:预测加工', name: '预测加工', category: '次级概念', color: '#E67E22' },
  { id: 'concept:绵延', name: '绵延', category: '次级概念', color: '#E67E22' },
  { id: 'concept:时间', name: '时间', category: '次级概念', color: '#E67E22' },
  { id: 'concept:历史性', name: '历史性', category: '次级概念', color: '#E67E22' },
  { id: 'concept:形态', name: '形态', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自因', name: '自因', category: '次级概念', color: '#E67E22' },
  { id: 'concept:单子', name: '单子', category: '次级概念', color: '#E67E22' },
  { id: 'concept:预定和谐', name: '预定和谐', category: '次级概念', color: '#E67E22' },
  { id: 'concept:耦合', name: '耦合', category: '次级概念', color: '#E67E22' },
  { id: 'concept:边界', name: '边界', category: '次级概念', color: '#E67E22' },
  { id: 'concept:消散', name: '消散', category: '次级概念', color: '#E67E22' },
  { id: 'concept:重生', name: '重生', category: '次级概念', color: '#E67E22' },
  { id: 'concept:感性', name: '感性', category: '次级概念', color: '#E67E22' },
  { id: 'concept:共振', name: '共振', category: '次级概念', color: '#E67E22' },
  { id: 'concept:临界点', name: '临界点', category: '次级概念', color: '#E67E22' },
  { id: 'concept:递归', name: '递归', category: '次级概念', color: '#E67E22' },

  // =================================================================
  // 3. 次级概念：社会、伦理与治理（橙色 #E67E22）
  // =================================================================
  { id: 'concept:成瘾', name: '成瘾', category: '次级概念', color: '#E67E22' },
  { id: 'concept:强势叙事', name: '强势叙事', category: '次级概念', color: '#E67E22' },
  { id: 'concept:伪漩涡', name: '伪漩涡', category: '次级概念', color: '#E67E22' },
  { id: 'concept:元讯息', name: '元讯息', category: '次级概念', color: '#E67E22' },
  { id: 'concept:双重束缚', name: '双重束缚', category: '次级概念', color: '#E67E22' },
  { id: 'concept:套套逻辑', name: '套套逻辑', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自反性', name: '自反性', category: '次级概念', color: '#E67E22' },
  { id: 'concept:教条', name: '教条', category: '次级概念', color: '#E67E22' },
  { id: 'concept:回到生活', name: '回到生活', category: '次级概念', color: '#E67E22' },
  { id: 'concept:所予神话', name: '所予神话', category: '次级概念', color: '#E67E22' },
  { id: 'concept:资本裹挟', name: '资本裹挟', category: '次级概念', color: '#E67E22' },
  { id: 'concept:绝对精神', name: '绝对精神', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自由意志', name: '自由意志', category: '次级概念', color: '#E67E22' },
  { id: 'concept:规范', name: '规范', category: '次级概念', color: '#E67E22' },
  { id: 'concept:元层通道', name: '元层通道', category: '次级概念', color: '#E67E22' },
  { id: 'concept:选票悖论', name: '选票悖论', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自我', name: '自我', category: '次级概念', color: '#E67E22' },
  { id: 'concept:叙事', name: '叙事', category: '次级概念', color: '#E67E22' },
  { id: 'concept:语言', name: '语言', category: '次级概念', color: '#E67E22' },
  { id: 'concept:根茎', name: '根茎', category: '次级概念', color: '#E67E22' },
  { id: 'concept:过程哲学', name: '过程哲学', category: '次级概念', color: '#E67E22' },
  { id: 'concept:现实事态', name: '现实事态', category: '次级概念', color: '#E67E22' },
  { id: 'concept:合生', name: '合生', category: '次级概念', color: '#E67E22' },
  { id: 'concept:生命冲动', name: '生命冲动', category: '次级概念', color: '#E67E22' },
  { id: 'concept:游戏哲学', name: '游戏哲学', category: '次级概念', color: '#E67E22' },
  { id: 'concept:沟通', name: '沟通', category: '次级概念', color: '#E67E22' },
  { id: 'concept:说得着', name: '说得着', category: '次级概念', color: '#E67E22' },
  { id: 'concept:文明', name: '文明', category: '次级概念', color: '#E67E22' },
  { id: 'concept:业力', name: '业力', category: '次级概念', color: '#E67E22' },
  { id: 'concept:免疫机制', name: '免疫机制', category: '次级概念', color: '#E67E22' },
  { id: 'concept:权力', name: '权力', category: '次级概念', color: '#E67E22' },
  { id: 'concept:制度筛选', name: '制度筛选', category: '次级概念', color: '#E67E22' },
  { id: 'concept:规训', name: '规训', category: '次级概念', color: '#E67E22' },
  { id: 'concept:生命政治', name: '生命政治', category: '次级概念', color: '#E67E22' },
  { id: 'concept:正常与异常', name: '正常与异常', category: '次级概念', color: '#E67E22' },

  // =================================================================
  // 4. 次级概念：哲学范畴与认识论（橙色 #E67E22）
  // =================================================================
  { id: 'concept:认识论', name: '认识论', category: '次级概念', color: '#E67E22' }, // 补全
  { id: 'concept:物自体', name: '物自体', category: '次级概念', color: '#E67E22' }, // 补全
  { id: 'concept:意识形态', name: '意识形态', category: '次级概念', color: '#E67E22' },
  { id: 'concept:幻象', name: '幻象', category: '次级概念', color: '#E67E22' },
  { id: 'concept:裂缝', name: '裂缝', category: '次级概念', color: '#E67E22' },
  { id: 'concept:实在界', name: '实在界', category: '次级概念', color: '#E67E22' },
  { id: 'concept:犬儒主义', name: '犬儒主义', category: '次级概念', color: '#E67E22' },
  { id: 'concept:事件', name: '事件', category: '次级概念', color: '#E67E22' },
  { id: 'concept:忠诚', name: '忠诚', category: '次级概念', color: '#E67E22' },
  { id: 'concept:数学本体论', name: '数学本体论', category: '次级概念', color: '#E67E22' },
  { id: 'concept:集合论', name: '集合论', category: '次级概念', color: '#E67E22' },
  { id: 'concept:斗争', name: '斗争', category: '次级概念', color: '#E67E22' },
  { id: 'concept:双重咬合', name: '双重咬合', category: '次级概念', color: '#E67E22' },
  { id: 'concept:否定之否定', name: '否定之否定', category: '次级概念', color: '#E67E22' },
  { id: 'concept:主次矛盾', name: '主次矛盾', category: '次级概念', color: '#E67E22' },
  { id: 'concept:爱', name: '爱', category: '次级概念', color: '#E67E22' },
  { id: 'concept:艺术', name: '艺术', category: '次级概念', color: '#E67E22' },
  { id: 'concept:光晕', name: '光晕', category: '次级概念', color: '#E67E22' },
  { id: 'concept:陌生化', name: '陌生化', category: '次级概念', color: '#E67E22' },
  { id: 'concept:治理', name: '治理', category: '次级概念', color: '#E67E22' },
  { id: 'concept:选票', name: '选票', category: '次级概念', color: '#E67E22' },
  { id: 'concept:民主', name: '民主', category: '次级概念', color: '#E67E22' },
  { id: 'concept:免疫系统', name: '免疫系统', category: '次级概念', color: '#E67E22' },
  { id: 'concept:僵化三角', name: '僵化三角', category: '次级概念', color: '#E67E22' },
  { id: 'concept:宗教', name: '宗教', category: '次级概念', color: '#E67E22' },
  { id: 'concept:绝对化', name: '绝对化', category: '次级概念', color: '#E67E22' },
  { id: 'concept:神话叙事', name: '神话叙事', category: '次级概念', color: '#E67E22' },
  { id: 'concept:黑暗根基', name: '黑暗根基', category: '次级概念', color: '#E67E22' },
  { id: 'concept:自由', name: '自由', category: '次级概念', color: '#E67E22' },
  { id: 'concept:匮乏', name: '匮乏', category: '次级概念', color: '#E67E22' },
  { id: 'concept:否定性', name: '否定性', category: '次级概念', color: '#E67E22' },
  { id: 'concept:肯定性', name: '肯定性', category: '次级概念', color: '#E67E22' },
  { id: 'concept:应然', name: '应然', category: '次级概念', color: '#E67E22' },
  { id: 'concept:实然', name: '实然', category: '次级概念', color: '#E67E22' },
  { id: 'concept:功能性规范', name: '功能性规范', category: '次级概念', color: '#E67E22' },
  { id: 'concept:差异', name: '差异', category: '次级概念', color: '#E67E22' },
  { id: 'concept:解域化', name: '解域化', category: '次级概念', color: '#E67E22' },
  { id: 'concept:装配', name: '装配', category: '次级概念', color: '#E67E22' },
  { id: 'concept:精神分裂', name: '精神分裂', category: '次级概念', color: '#E67E22' },
  { id: 'concept:语言游戏', name: '语言游戏', category: '次级概念', color: '#E67E22' },
  { id: 'concept:家族相似', name: '家族相似', category: '次级概念', color: '#E67E22' },
  { id: 'concept:可说与不可说', name: '可说与不可说', category: '次级概念', color: '#E67E22' },
  { id: 'concept:元层', name: '元层', category: '次级概念', color: '#E67E22' }, // 补全

  // =================================================================
  // 5. 哲学家（蓝色 #2980B9）—— 思想的对话者
  // =================================================================
  { id: 'concept:德勒兹', name: '德勒兹', category: '哲学家', color: '#2980B9' },
  { id: 'concept:齐泽克', name: '齐泽克', category: '哲学家', color: '#2980B9' },
  { id: 'concept:巴迪欧', name: '巴迪欧', category: '哲学家', color: '#2980B9' },
  { id: 'concept:怀特海', name: '怀特海', category: '哲学家', color: '#2980B9' },
  { id: 'concept:柏格森', name: '柏格森', category: '哲学家', color: '#2980B9' },
  { id: 'concept:贝特森', name: '贝特森', category: '哲学家', color: '#2980B9' },
  { id: 'concept:康德', name: '康德', category: '哲学家', color: '#2980B9' },
  { id: 'concept:尼采', name: '尼采', category: '哲学家', color: '#2980B9' },
  { id: 'concept:马克思', name: '马克思', category: '哲学家', color: '#2980B9' },
  { id: 'concept:维特根斯坦', name: '维特根斯坦', category: '哲学家', color: '#2980B9' },
  { id: 'concept:谢林', name: '谢林', category: '哲学家', color: '#2980B9' },
  { id: 'concept:笛卡尔', name: '笛卡尔', category: '哲学家', color: '#2980B9' },
  { id: 'concept:斯宾诺莎', name: '斯宾诺莎', category: '哲学家', color: '#2980B9' },
  { id: 'concept:莱布尼茨', name: '莱布尼茨', category: '哲学家', color: '#2980B9' },
  { id: 'concept:胡塞尔', name: '胡塞尔', category: '哲学家', color: '#2980B9' },
  { id: 'concept:梅洛庞蒂', name: '梅洛-庞蒂', category: '哲学家', color: '#2980B9' },
  { id: 'concept:拉康', name: '拉康', category: '哲学家', color: '#2980B9' },
  { id: 'concept:福柯', name: '福柯', category: '哲学家', color: '#2980B9' },
  { id: 'concept:阿多诺', name: '阿多诺', category: '哲学家', color: '#2980B9' },
  { id: 'concept:列维纳斯', name: '列维纳斯', category: '哲学家', color: '#2980B9' },
  { id: 'concept:莫兰', name: '莫兰', category: '哲学家', color: '#2980B9' },
  { id: 'concept:瓦雷拉', name: '瓦雷拉', category: '哲学家', color: '#2980B9' },
  { id: 'concept:塞拉斯', name: '塞拉斯', category: '哲学家', color: '#2980B9' },
  { id: 'concept:罗韦利', name: '罗韦利', category: '哲学家', color: '#2980B9' },
  { id: 'concept:侯世达', name: '侯世达', category: '哲学家', color: '#2980B9' },
  { id: 'concept:普里高津', name: '普里高津', category: '哲学家', color: '#2980B9' },
  { id: 'concept:龙树', name: '龙树', category: '哲学家', color: '#2980B9' },
  { id: 'concept:香农', name: '香农', category: '哲学家', color: '#2980B9' },
  { id: 'concept:麦克卢汉', name: '麦克卢汉', category: '哲学家', color: '#2980B9' },
  { id: 'concept:西蒙东', name: '西蒙东', category: '哲学家', color: '#2980B9' },
  { id: 'concept:阿西莫格鲁', name: '阿西莫格鲁', category: '哲学家', color: '#2980B9' },
  { id: 'concept:休谟', name: '休谟', category: '哲学家', color: '#2980B9' },
  { id: 'concept:亨廷顿', name: '亨廷顿', category: '哲学家', color: '#2980B9' },
  { id: 'concept:拉图尔', name: '拉图尔', category: '哲学家', color: '#2980B9' },
  { id: 'concept:黑格尔', name: '黑格尔', category: '哲学家', color: '#2980B9' },

  // =================================================================
  // 6. 东方思想（蓝绿色 #1ABC9C）
  // =================================================================
  { id: 'concept:道家', name: '道家', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:儒家', name: '儒家', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:禅宗', name: '禅宗', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:缘起', name: '缘起', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:空', name: '空', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:中道', name: '中道', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:四句破', name: '四句破', category: '东方思想', color: '#1ABC9C' },
  { id: 'concept:解脱', name: '解脱', category: '东方思想', color: '#1ABC9C' },

  // =================================================================
  // 7. 案例与印证（绿色 #27AE60）
  // =================================================================
  { id: 'concept:赤名莉香', name: '赤名莉香', category: '案例', color: '#27AE60' },
  { id: 'concept:四个春天', name: '《四个春天》', category: '案例', color: '#27AE60' },
  { id: 'concept:大明1566', name: '《大明1566》', category: '案例', color: '#27AE60' },
  { id: 'concept:荆棘鸟', name: '《荆棘鸟》', category: '案例', color: '#27AE60' },
  { id: 'concept:廊桥遗梦', name: '《廊桥遗梦》', category: '案例', color: '#27AE60' },
  { id: 'concept:东京爱情故事', name: '《东京爱情故事》', category: '案例', color: '#27AE60' },
  { id: 'concept:一句顶一万句', name: '《一句顶一万句》', category: '案例', color: '#27AE60' },
  { id: 'concept:火焰纹章', name: '《火焰纹章》', category: '案例', color: '#27AE60' },
  { id: 'concept:开源社区', name: '开源社区', category: '案例', color: '#27AE60' },
  { id: 'concept:即兴爵士乐队', name: '即兴爵士乐队', category: '案例', color: '#27AE60' },
  { id: 'concept:刘震云', name: '刘震云', category: '案例', color: '#27AE60' },
  { id: 'concept:塞尚', name: '塞尚', category: '案例', color: '#27AE60' },
  { id: 'concept:巴赫', name: '巴赫', category: '案例', color: '#27AE60' },
  { id: 'concept:本雅明', name: '本雅明', category: '案例', color: '#27AE60' },
  { id: 'concept:什克洛夫斯基', name: '什克洛夫斯基', category: '案例', color: '#27AE60' },
  { id: 'concept:米拉', name: '米拉', category: '案例', color: '#27AE60' },
  { id: 'concept:多玛', name: '多玛', category: '案例', color: '#27AE60' },
];

// ============================================================
// 二、关系定义（LINKS）
// 按「五条主线 + 哲学家映射 + 核心张力 + 案例印证」分区
// ============================================================
const CONCEPT_RELATIONS = [

  // =================================================================
  // 【主线一】本体论核心线：关系 → 信息/生成 → 涌现 → 漩涡 → 下行因果
  // =================================================================
  { source: 'concept:关系', target: 'concept:信息', type: '构成' },
  { source: 'concept:关系', target: 'concept:生成', type: '构成' },
  { source: 'concept:信息', target: 'concept:生成', type: '缠绕' },   // 二者不可分割
  { source: 'concept:生成', target: 'concept:涌现', type: '包含' },   // 涌现是生成的临界质变
  { source: 'concept:关系', target: 'concept:涌现', type: '构成' },
  { source: 'concept:上行因果', target: 'concept:涌现', type: '导致' },
  { source: 'concept:涌现', target: 'concept:下行因果', type: '产生' },
  { source: 'concept:涌现', target: 'concept:漩涡', type: '事件标记' }, // 涌现是诞生的那一刻
  { source: 'concept:漩涡', target: 'concept:动态平衡', type: '构成' },
  { source: 'concept:自指', target: 'concept:漩涡', type: '构成' },
  { source: 'concept:关系第一性', target: 'concept:关系', type: '构成' },
  { source: 'concept:上行因果', target: 'concept:漩涡', type: '构成' },
  { source: 'concept:下行因果', target: 'concept:漩涡', type: '构成' },
  { source: 'concept:选择性张力', target: 'concept:动态平衡', type: '构成' },
  { source: 'concept:开放性', target: 'concept:动态平衡', type: '条件' },
  // —— 系统科学对涌现的支撑 ——
  { source: 'concept:自组织', target: 'concept:涌现', type: '条件' },
  { source: 'concept:自创生', target: 'concept:涌现', type: '实现' },
  { source: 'concept:开放性', target: 'concept:涌现', type: '条件' },
  { source: 'concept:动态平衡', target: 'concept:涌现', type: '触发' },
  { source: 'concept:自指', target: 'concept:涌现', type: '产生' },
  { source: 'concept:贝纳德对流', target: 'concept:涌现', type: '触发' },
  { source: 'concept:临界点', target: 'concept:涌现', type: '触发' },
  { source: 'concept:信息', target: 'concept:涌现', type: '构成' },

  // =================================================================
  // 【主线二】认识论转向线：所予神话 → 涌现（范式转换）
  // =================================================================
  { source: 'concept:认识论', target: 'concept:所予神话', type: '批判' },
  { source: 'concept:所予神话', target: 'concept:涌现', type: '超越' },
  { source: 'concept:认识论', target: 'concept:涌现', type: '转向' },

  // =================================================================
  // 【主线三】文明演化线：河床 → 规范 → 僵化 → 递归 → 业力 → 元层通道
  // =================================================================
  { source: 'concept:亨廷顿', target: 'concept:文明', type: '批判' },
  { source: 'concept:亨廷顿', target: 'concept:河床', type: '超越' },
  { source: 'concept:文明', target: 'concept:河床', type: '比喻' },
  { source: 'concept:文明', target: 'concept:规范', type: '构成' },
  { source: 'concept:规范', target: 'concept:僵化', type: '趋向' },
  { source: 'concept:僵化', target: 'concept:韧性', type: '对立' },
  { source: 'concept:僵化', target: 'concept:递归', type: '触发' },
  { source: 'concept:递归', target: 'concept:元层通道', type: '构成' },
  // —— 业力作为文明沉积物 ——
  { source: 'concept:业力', target: 'concept:文明', type: '构成' },
  { source: 'concept:业力', target: 'concept:河床', type: '比喻' },
  { source: 'concept:业力', target: 'concept:规范', type: '构成' },
  { source: 'concept:业力', target: 'concept:僵化', type: '导致' },
  { source: 'concept:业力', target: 'concept:递归', type: '循环' },
  { source: 'concept:业力', target: 'concept:下行因果', type: '构成' },
  { source: 'concept:业力', target: 'concept:元层通道', type: '阻塞' },
  { source: 'concept:业力', target: 'concept:选票悖论', type: '解释' },
  // —— 福柯权力解剖学：规范的生产与元层的阻塞（第六章文明演化支撑） ——
  { source: 'concept:福柯', target: 'concept:下行因果', type: '形态' },
  { source: 'concept:福柯', target: 'concept:规范', type: '生产' },
  { source: 'concept:福柯', target: 'concept:僵化', type: '导致' },
  { source: 'concept:福柯', target: 'concept:元层通道', type: '阻塞' },
  { source: 'concept:规训', target: 'concept:选择性张力', type: '类比' },
  { source: 'concept:生命政治', target: 'concept:文明', type: '治理' },
   // —— 福柯：正常与异常的规范化生产（新增哲学对话福柯章） ——
  { source: 'concept:福柯', target: 'concept:正常与异常', type: '奠基' },
  { source: 'concept:规训', target: 'concept:正常与异常', type: '生产' },
  { source: 'concept:权力', target: 'concept:正常与异常', type: '生产' },
  { source: 'concept:生命政治', target: 'concept:正常与异常', type: '治理' },
  { source: 'concept:正常与异常', target: 'concept:规范', type: '构成' },
  { source: 'concept:正常与异常', target: 'concept:僵化', type: '趋向' },

  // —— 福柯与权力概念的重构（权力作为关系性力量场） ——
  { source: 'concept:福柯', target: 'concept:权力', type: '奠基' },
  { source: 'concept:权力', target: 'concept:规训', type: '机制' },
  { source: 'concept:权力', target: 'concept:生命政治', type: '演变' },
  { source: 'concept:权力', target: 'concept:规范', type: '生产' },
  { source: 'concept:权力', target: 'concept:资本裹挟', type: '缠绕' },
  { source: 'concept:权力', target: 'concept:元层通道', type: '阻塞' },

  // =================================================================
  // 【主线四】元层与治理线：选票悖论 → 元层通道 → 自指 / 下行因果
  // =================================================================
  { source: 'concept:选票悖论', target: 'concept:元层通道', type: '揭示' },
  { source: 'concept:选票悖论', target: 'concept:制度筛选', type: '揭示' },
  { source: 'concept:元层通道', target: 'concept:自指', type: '类比' },
  { source: 'concept:元层通道', target: 'concept:下行因果', type: '类比' },
  { source: 'concept:元层', target: 'concept:自指', type: '构成' },
  { source: 'concept:递归', target: 'concept:自指', type: '构成' },
  { source: 'concept:元层通道', target: 'concept:递归', type: '构成' },

  // =================================================================
  // 【主线五】哲学对话线：休谟 → 裂缝 → 实然/应然 → 功能性规范
  // =================================================================
  { source: 'concept:休谟', target: 'concept:裂缝', type: '奠基' },
  { source: 'concept:裂缝', target: 'concept:实然', type: '张力' },
  { source: 'concept:裂缝', target: 'concept:应然', type: '张力' },
  { source: 'concept:功能性规范', target: 'concept:应然', type: '构成' },

  // =================================================================
  // 【哲学家 → 概念】映射（奠基 / 共鸣 / 批判）
  // =================================================================
  // —— 德勒兹：差异、生成与解域化 ——
  { source: 'concept:德勒兹', target: 'concept:生成', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:自组织', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:差异', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:根茎', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:解域化', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:装配', type: '共鸣' },
  { source: 'concept:德勒兹', target: 'concept:精神分裂', type: '共鸣' },
  { source: 'concept:根茎', target: 'concept:解域化', type: '构成' },
  { source: 'concept:装配', target: 'concept:解域化', type: '构成' },

  // —— 贝特森：信息、逻辑类型与元讯息 ——
  { source: 'concept:贝特森', target: 'concept:信息', type: '奠基' },
  { source: 'concept:贝特森', target: 'concept:自指', type: '奠基' },
  { source: 'concept:贝特森', target: 'concept:逻辑类型', type: '奠基' },
  { source: 'concept:贝特森', target: 'concept:元讯息', type: '奠基' },
  { source: 'concept:贝特森', target: 'concept:双重束缚', type: '奠基' },

  // —— 怀特海：关系、过程与合生 ——
  { source: 'concept:怀特海', target: 'concept:关系', type: '奠基' },
  { source: 'concept:怀特海', target: 'concept:动态平衡', type: '奠基' },
  { source: 'concept:怀特海', target: 'concept:过程哲学', type: '奠基' },
  { source: 'concept:怀特海', target: 'concept:现实事态', type: '奠基' },
  { source: 'concept:怀特海', target: 'concept:合生', type: '奠基' },

  // —— 柏格森：绵延与生命冲动 ——
  { source: 'concept:柏格森', target: 'concept:生成', type: '奠基' },
  { source: 'concept:柏格森', target: 'concept:绵延', type: '奠基' },
  { source: 'concept:柏格森', target: 'concept:生命冲动', type: '奠基' },
  { source: 'concept:柏格森', target: 'concept:形态', type: '奠基' },

  // —— 齐泽克：裂缝、意识形态与实在界 ——
  { source: 'concept:齐泽克', target: 'concept:自指', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:下行因果', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:意识形态', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:裂缝', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:幻象', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:实在界', type: '批判' },
  { source: 'concept:齐泽克', target: 'concept:犬儒主义', type: '批判' },

  // —— 康德：自律与先验范畴 ——
  { source: 'concept:康德', target: 'concept:自指', type: '奠基' },
  { source: 'concept:康德', target: 'concept:自律', type: '奠基' },
  { source: 'concept:康德', target: 'concept:先验范畴', type: '奠基' },
  { source: 'concept:康德', target: 'concept:道德法则', type: '奠基' },
  { source: 'concept:康德', target: 'concept:物自体', type: '奠基' },

  // —— 尼采：权力意志与永恒回归 ——
  { source: 'concept:尼采', target: 'concept:生成', type: '共鸣' },
  { source: 'concept:尼采', target: 'concept:动态平衡', type: '共鸣' },
  { source: 'concept:尼采', target: 'concept:权力意志', type: '共鸣' },
  { source: 'concept:尼采', target: 'concept:永恒回归', type: '共鸣' },
  { source: 'concept:尼采', target: 'concept:悲剧', type: '共鸣' },
  { source: 'concept:尼采', target: 'concept:超人', type: '共鸣' },

  // —— 马克思：下行因果与斗争 ——
  { source: 'concept:马克思', target: 'concept:下行因果', type: '奠基' },
  { source: 'concept:马克思', target: 'concept:资本裹挟', type: '奠基' },
  { source: 'concept:马克思', target: 'concept:斗争', type: '奠基' },
  { source: 'concept:马克思', target: 'concept:双重咬合', type: '奠基' },
  { source: 'concept:马克思', target: 'concept:否定之否定', type: '奠基' },
  { source: 'concept:马克思', target: 'concept:主次矛盾', type: '奠基' },

  // —— 维特根斯坦：语言游戏与家族相似 ——
  { source: 'concept:维特根斯坦', target: 'concept:关系', type: '共鸣' },
  { source: 'concept:维特根斯坦', target: 'concept:语言', type: '共鸣' },
  { source: 'concept:维特根斯坦', target: 'concept:语言游戏', type: '共鸣' },
  { source: 'concept:维特根斯坦', target: 'concept:家族相似', type: '共鸣' },
  { source: 'concept:维特根斯坦', target: 'concept:可说与不可说', type: '共鸣' },

  // —— 其他哲学家 ——
  { source: 'concept:谢林', target: 'concept:黑暗根基', type: '奠基' },
  { source: 'concept:谢林', target: 'concept:否定性', type: '奠基' },
  { source: 'concept:谢林', target: 'concept:自由', type: '奠基' },
  { source: 'concept:拉康', target: 'concept:自我', type: '奠基' },
  { source: 'concept:拉康', target: 'concept:匮乏', type: '奠基' },
  { source: 'concept:胡塞尔', target: 'concept:认知', type: '奠基' },
  { source: 'concept:梅洛庞蒂', target: 'concept:认知', type: '奠基' },
  { source: 'concept:瓦雷拉', target: 'concept:自创生', type: '奠基' },
  { source: 'concept:普里高津', target: 'concept:耗散结构', type: '奠基' },
  { source: 'concept:普里高津', target: 'concept:非平衡态', type: '奠基' },
  { source: 'concept:普里高津', target: 'concept:自组织', type: '奠基' },
  { source: 'concept:侯世达', target: 'concept:怪圈', type: '奠基' },
  { source: 'concept:侯世达', target: 'concept:自指', type: '奠基' },
  { source: 'concept:塞拉斯', target: 'concept:所予神话', type: '奠基' },
  { source: 'concept:塞拉斯', target: 'concept:认知', type: '奠基' },
  { source: 'concept:罗韦利', target: 'concept:协变量子场', type: '奠基' },
  { source: 'concept:罗韦利', target: 'concept:量子纠缠', type: '奠基' },
  { source: 'concept:拉图尔', target: 'concept:关系', type: '奠基' },
  { source: 'concept:福柯', target: 'concept:资本裹挟', type: '批判' },
  { source: 'concept:阿多诺', target: 'concept:僵化', type: '批判' },
  { source: 'concept:列维纳斯', target: 'concept:他者开放性', type: '奠基' },
  { source: 'concept:巴迪欧', target: 'concept:事件', type: '奠基' },
  { source: 'concept:巴迪欧', target: 'concept:忠诚', type: '奠基' },
  { source: 'concept:巴迪欧', target: 'concept:数学本体论', type: '奠基' },
  { source: 'concept:巴迪欧', target: 'concept:集合论', type: '共鸣' },
  { source: 'concept:莫兰', target: 'concept:上行因果', type: '共鸣' },
  { source: 'concept:莫兰', target: 'concept:下行因果', type: '共鸣' },
  { source: 'concept:香农', target: 'concept:信息', type: '奠基' },
  { source: 'concept:麦克卢汉', target: 'concept:信息', type: '奠基' },
  { source: 'concept:西蒙东', target: 'concept:生成', type: '奠基' },
  { source: 'concept:阿西莫格鲁', target: 'concept:治理', type: '批判' },
  { source: 'concept:黑格尔', target: 'concept:绝对精神', type: '奠基' },

  // =================================================================
  // 【东方思想】与漩涡的共鸣
  // =================================================================
  { source: 'concept:缘起', target: 'concept:关系第一性', type: '共鸣' },
  { source: 'concept:龙树', target: 'concept:空', type: '奠基' },
  { source: 'concept:龙树', target: 'concept:中道', type: '奠基' },
  { source: 'concept:龙树', target: 'concept:四句破', type: '奠基' },
  { source: 'concept:禅宗', target: 'concept:自指', type: '共鸣' },
  { source: 'concept:道家', target: 'concept:关系', type: '共鸣' },
  { source: 'concept:儒家', target: 'concept:关系', type: '共鸣' },

  // =================================================================
  // 【核心概念之间的张力与循环】
  // =================================================================
  { source: 'concept:信息', target: 'concept:生成', type: '缠绕' },
  { source: 'concept:上行因果', target: 'concept:下行因果', type: '循环' },
  { source: 'concept:自组织', target: 'concept:自创生', type: '递进' },
  { source: 'concept:自创生', target: 'concept:自指', type: '递进' },
  { source: 'concept:肯定性', target: 'concept:否定性', type: '张力' },
  { source: 'concept:实体论', target: 'concept:关系第一性', type: '超越' },
  { source: 'concept:僵化', target: 'concept:韧性', type: '对立' },
  { source: 'concept:裂缝', target: 'concept:实然', type: '张力' },
  { source: 'concept:裂缝', target: 'concept:应然', type: '张力' },
  { source: 'concept:河床', target: 'concept:漩涡', type: '比喻' },
  { source: 'concept:递归', target: 'concept:生成', type: '共鸣' },
  { source: 'concept:功能性规范', target: 'concept:规范', type: '派生' },
  { source: 'concept:韧性', target: 'concept:涌现', type: '回应' },
  { source: 'concept:成瘾', target: 'concept:僵化', type: '趋向' },
  { source: 'concept:强势叙事', target: 'concept:僵化', type: '趋向' },
  { source: 'concept:爱', target: 'concept:动态平衡', type: '构成' },

  // =================================================================
  // 【案例印证】理论在具体现象中的落地
  // =================================================================
  { source: 'concept:赤名莉香', target: 'concept:动态平衡', type: '印证' },
  { source: 'concept:赤名莉香', target: 'concept:爱', type: '印证' },
  { source: 'concept:四个春天', target: 'concept:选择性张力', type: '印证' },
  { source: 'concept:四个春天', target: 'concept:动态平衡', type: '印证' },
  { source: 'concept:四个春天', target: 'concept:韧性', type: '印证' },
  { source: 'concept:大明1566', target: 'concept:下行因果', type: '印证' },
  { source: 'concept:大明1566', target: 'concept:僵化', type: '印证' },
  { source: 'concept:荆棘鸟', target: 'concept:生成', type: '印证' },
  { source: 'concept:荆棘鸟', target: 'concept:爱', type: '印证' },
  { source: 'concept:廊桥遗梦', target: 'concept:僵化', type: '印证' },
  { source: 'concept:东京爱情故事', target: 'concept:爱', type: '印证' },
  { source: 'concept:一句顶一万句', target: 'concept:关系', type: '印证' },
  { source: 'concept:一句顶一万句', target: 'concept:共振', type: '印证' },
  { source: 'concept:一句顶一万句', target: 'concept:沟通', type: '印证' },
  { source: 'concept:火焰纹章', target: 'concept:僵化', type: '印证' },
  { source: 'concept:火焰纹章', target: 'concept:绝对化', type: '印证' },
  { source: 'concept:开源社区', target: 'concept:上行因果', type: '印证' },
  { source: 'concept:开源社区', target: 'concept:下行因果', type: '印证' },
  { source: 'concept:开源社区', target: 'concept:自组织', type: '印证' },
  { source: 'concept:即兴爵士乐队', target: 'concept:选择性张力', type: '印证' },
  { source: 'concept:塞尚', target: 'concept:艺术', type: '印证' },
  { source: 'concept:巴赫', target: 'concept:艺术', type: '印证' },
  { source: 'concept:亨廷顿', target: 'concept:选票悖论', type: '相关' }, // 跨线连接
  { source: 'concept:裂缝', target: 'concept:下行因果', type: '类比' },   // 跨线连接
];
    // ============================================================
    // 2. 收集文章数据（Jekyll 渲染）
    // ============================================================
    const posts = [
      {% assign graph_posts = site.posts | where_exp: "post", "post.published != false" | sort: "date" | reverse | slice: 0, 120 %}
      {% for post in graph_posts %}
      {
        id: {{ post.url | relative_url | jsonify }},
        title: {{ post.title | jsonify }},
        url: {{ post.url | relative_url | jsonify }},
        categories: [{% for category in post.categories %}{{ category | jsonify }}{% if forloop.last == false %}, {% endif %}{% endfor %}],
        tags: [{% for tag in post.tags %}{{ tag | jsonify }}{% if forloop.last == false %}, {% endif %}{% endfor %}],
        concepts: [{% for concept in post.concepts %}{{ concept | jsonify }}{% if forloop.last == false %}, {% endif %}{% endfor %}]
      }{% if forloop.last == false %},{% endif %}
      {% endfor %}
    ];


    // ============================================================
    // 3. 构建节点与边
    // ============================================================
    const nodeMap = new Map();
    const links = [];

    CONCEPT_DEFINITIONS.forEach(function(def) {
      nodeMap.set(def.id, {
        id: def.id,
        name: def.name,
        category: def.category,
        color: def.color,
        symbolSize: def.category === '核心概念' ? 48 :
                     def.category === '哲学家' ? 40 :
                     def.category === '次级概念' ? 32 : 28,
        value: 1,
        label: { fontSize: def.category === '核心概念' ? 13 :
                         def.category === '哲学家' ? 12 : 10 },
      });
    });

    CONCEPT_RELATIONS.forEach(function(rel) {
      if (nodeMap.has(rel.source) && nodeMap.has(rel.target)) {
        links.push({
          source: rel.source,
          target: rel.target,
          value: 1,
          type: rel.type,
          label: { show: true, formatter: rel.type, fontSize: 9, color: '#888' }
        });
      }
    });

    const categoryNodes = new Map();
    const tagNodes = new Map();
    const sectionNodes = new Map();

    posts.forEach(function(post) {
      nodeMap.set(post.id, {
        id: post.id,
        name: post.title,
        category: '文章',
        symbolSize: 38,
        url: post.url,
        value: post.categories.length + post.tags.length + 1,
        label: { fontSize: 12 }
      });

      post.categories.forEach(function(category) {
        const nodeId = 'category:' + category;
        if (!categoryNodes.has(nodeId)) {
          categoryNodes.set(nodeId, {
            id: nodeId,
            name: category,
            category: '分类',
            symbolSize: 22,
            value: 1,
            label: { fontSize: 10 }
          });
        } else {
          categoryNodes.get(nodeId).value += 1;
        }
        links.push({ source: post.id, target: nodeId, value: 1 });
      });

      post.tags.forEach(function(tag) {
        const nodeId = 'tag:' + tag;
        if (!tagNodes.has(nodeId)) {
          tagNodes.set(nodeId, {
            id: nodeId,
            name: tag,
            category: '标签',
            symbolSize: 18,
            value: 1,
            label: { fontSize: 10 }
          });
        } else {
          tagNodes.get(nodeId).value += 1;
        }
        links.push({ source: post.id, target: nodeId, value: 1 });
      });

      if (post.concepts) {
        post.concepts.forEach(function(conceptName) {
          const conceptId = 'concept:' + conceptName;
          if (nodeMap.has(conceptId)) {
            links.push({ source: post.id, target: conceptId, value: 1 });
          }
        });
      }
    });

    const allNodes = [
      ...Array.from(nodeMap.values()),
      ...Array.from(categoryNodes.values()),
      ...Array.from(tagNodes.values()),
      ...Array.from(sectionNodes.values())
    ];

    allNodes.forEach(function(node) {
      if (node.category === '分类') {
        node.symbolSize = 22 + Math.min(node.value || 1, 8);
        node.itemStyle = { color: PALETTE.category };
      } else if (node.category === '标签') {
        node.symbolSize = 18 + Math.min(node.value || 1, 6);
        node.itemStyle = { color: PALETTE.tag };
      } else if (node.category === '章节') {
        node.symbolSize = 14 + Math.min(node.value || 1, 6);
        node.itemStyle = { color: PALETTE.section };
      } else if (node.category === '核心概念') {
        node.itemStyle = { color: PALETTE.core };
      } else if (node.category === '次级概念') {
        node.itemStyle = { color: PALETTE.secondary };
      } else if (node.category === '哲学家') {
        node.itemStyle = { color: PALETTE.philosopher };
      } else if (node.category === '案例') {
        node.itemStyle = { color: PALETTE.case };
        node.symbol = 'triangle';
      } else if (node.category === '文章') {
        node.itemStyle = { color: PALETTE.article };
      } else {
        node.itemStyle = { color: PALETTE.default };
      }
    });

    const allLinks = links.slice();

    let currentNodes = allNodes;
    let currentLinks = allLinks;


    // ============================================================
    // 4. 提取文章章节
    // ============================================================
    function slugify(text) {
      return text.toLowerCase()
        .trim()
        .replace(/[^\w\u4e00-\u9fff\- ]+/g, '')
        .replace(/\s+/g, '-')
        .replace(/-+/g, '-');
    }

    const fetchSections = posts.map(function(post) {
      return fetch(post.url, { credentials: 'same-origin' })
        .then(function(response) {
          if (!response.ok) throw new Error('Network error');
          return response.text();
        })
        .then(function(html) {
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          const sectionTitles = Array.from(
            doc.querySelectorAll('article.post .post-content h1, article.post .post-content h2, article.post .post-content h3')
          );
          sectionTitles.forEach(function(section, index) {
            const sectionText = section.textContent.trim();
            if (!sectionText) return;
            const headingId = section.id || slugify(sectionText);
            const nodeId = post.id + ':section:' + index;
            sectionNodes.set(nodeId, {
              id: nodeId,
              name: sectionText,
              category: '章节',
              parentTitle: post.title,
              url: post.url + '#' + headingId,
              symbolSize: 16,
              label: { fontSize: 9 },
              itemStyle: { color: '#2ECC71' }
            });
            allNodes.push(sectionNodes.get(nodeId));
            allLinks.push({ source: post.id, target: nodeId, value: 1 });
          });
        })
        .catch(function() {
          // 忽略抓取错误
        });
    });


    // ============================================================
    // 5. 渲染 ECharts 图谱
    // ============================================================
    Promise.all(fetchSections).then(function() {
      currentNodes = allNodes;
      currentLinks = allLinks;

      const chartDom = document.getElementById('knowledge-graph');
      const searchInput = document.getElementById('knowledge-graph-search');
      const resetButton = document.getElementById('knowledge-graph-reset');

      const myChart = echarts.init(chartDom);

      function renderGraph(nodes, linksData) {
        const option = {
          tooltip: {
            formatter: function(param) {
              if (param.dataType === 'edge') {
                const relType = param.data.type || '';
                return '<span style="color:#999;">关系：</span>' + (relType || '关联');
              }
              if (!param.data) return '';
              let html = '<strong>' + param.data.name + '</strong><br>';
              html += '类型：' + param.data.category;
              if (param.data.parentTitle) {
                html += '<br>所属文章：' + param.data.parentTitle;
              }
              if (param.data.url) {
                if (param.data.category === '文章') {
                  html += '<br><span style="color:#8E44AD;">点击跳转文章</span>';
                } else if (param.data.category === '章节') {
                  html += '<br><span style="color:#2ECC71;">点击跳转至该节</span>';
                }
              }
              return html;
            }
          },
          legend: [{
            data: ['文章', '分类', '标签', '章节', '核心概念', '次级概念', '哲学家', '案例'],
            orient: 'horizontal',
            bottom: 10,
            textStyle: { color: '#666', fontSize: 12 },
            formatter: function(name) {
              return name;
            }
          }],
          series: [{
            type: 'graph',
            layout: 'force',
            roam: true,
            draggable: true,
            animationDurationUpdate: 300,
            force: {
              repulsion: 280,
              edgeLength: [80, 200],
              gravity: 0.08
            },
            categories: [
              { name: '文章', itemStyle: { color: PALETTE.article } },
              { name: '分类', itemStyle: { color: PALETTE.category } },
              { name: '标签', itemStyle: { color: PALETTE.tag } },
              { name: '章节', itemStyle: { color: PALETTE.section } },
              { name: '核心概念', itemStyle: { color: PALETTE.core } },
              { name: '次级概念', itemStyle: { color: PALETTE.secondary } },
              { name: '哲学家', itemStyle: { color: PALETTE.philosopher } },
              { name: '案例', itemStyle: { color: PALETTE.case } }
            ],
            data: nodes,
            links: linksData,
            focusNodeAdjacency: true,
            emphasis: {
              focus: 'adjacency',
              label: { show: true, fontWeight: 'bold' }
            },
            label: {
              position: 'right',
              formatter: function(params) {
                return params.data ? params.data.name : '';
              },
              fontSize: 11,
              color: '#333'
            },
            lineStyle: {
              color: 'source',
              curveness: 0.2,
              opacity: 0.6
            },
            edgeLabel: {
              show: true,
              formatter: function(params) {
                return params.data.type || '';
              },
              fontSize: 9,
              color: '#888'
            }
          }]
        };
        myChart.setOption(option, true);
      }

      renderGraph(currentNodes, currentLinks);

      // ============================================================
      // 6. 点击跳转：文章 + 章节
      // ============================================================
      myChart.on('click', function(params) {
        if (!params.data || !params.data.url) return;
        // 文章和章节都可以跳转
        if (params.data.category === '文章' || params.data.category === '章节') {
          window.location.href = params.data.url;
        }
      });

      // 搜索过滤
      function applyFilter(query) {
        const normalized = query.trim().toLowerCase();
        if (!normalized) {
          currentNodes = allNodes;
          currentLinks = allLinks;
          renderGraph(currentNodes, currentLinks);
          return;
        }

        const matchedIds = new Set();
        allNodes.forEach(function(node) {
          const searchText = (node.name + ' ' + node.category + ' ' + (node.parentTitle || '')).toLowerCase();
          if (searchText.indexOf(normalized) >= 0) {
            matchedIds.add(node.id);
          }
        });

        const visibleIds = new Set(matchedIds);
        allLinks.forEach(function(link) {
          if (matchedIds.has(link.source) || matchedIds.has(link.target)) {
            visibleIds.add(link.source);
            visibleIds.add(link.target);
          }
        });

        currentNodes = allNodes.filter(function(node) {
          return visibleIds.has(node.id);
        });
        currentLinks = allLinks.filter(function(link) {
          return visibleIds.has(link.source) && visibleIds.has(link.target);
        });
        renderGraph(currentNodes, currentLinks);
      }

      searchInput.addEventListener('input', function() {
        applyFilter(this.value);
      });

      resetButton.addEventListener('click', function() {
        searchInput.value = '';
        applyFilter('');
      });

      window.addEventListener('resize', function() {
        myChart.resize();
      });
    });
  });
</script>