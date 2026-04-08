"""State models used by the deep research workflow."""

import operator
from dataclasses import dataclass, field
from typing import List, Optional

from typing_extensions import Annotated


@dataclass(kw_only=True)
class TodoItem:
    """单个待办任务项。"""

    id: int # 编号
    title: str  # 任务名
    intent: str # 研究意图
    query: str  # 查询关键词
    status: str = field(default="pending")  # 状态（排队中，进行中....)
    summary: Optional[str] = field(default=None)
    sources_summary: Optional[str] = field(default=None)
    notices: list[str] = field(default_factory=list)
    note_id: Optional[str] = field(default=None)
    note_path: Optional[str] = field(default=None)
    stream_token: Optional[str] = field(default=None)   # 属于哪一个任务的


@dataclass(kw_only=True)
class SummaryState:
    research_topic: str = field(default=None)  # 原始需求
    search_query: str = field(default=None)  # 查询关键词
    web_research_results: Annotated[list, operator.add] = field(default_factory=list)   # 结果
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list)   # 整理好的资料
    research_loop_count: int = field(default=0)  # 循环次数
    running_summary: str = field(default=None)
    todo_items: Annotated[list, operator.add] = field(default_factory=list) # 任务列表
    structured_report: Optional[str] = field(default=None)      # 最终报告
    report_note_id: Optional[str] = field(default=None)
    report_note_path: Optional[str] = field(default=None)


@dataclass(kw_only=True)
class SummaryStateInput:
    research_topic: str = field(default=None)  # Report topic


@dataclass(kw_only=True)
class SummaryStateOutput:
    running_summary: str = field(default=None)  # Backward-compatible文本
    report_markdown: Optional[str] = field(default=None)
    todo_items: List[TodoItem] = field(default_factory=list)

