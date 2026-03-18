from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):
	PENDING = "pending"
	IN_PROGRESS = "in_progress"
	COMPLETE = "complete"


class DeveloperTask(BaseModel):
	task_id: int
	title: str
	status: TaskStatus = TaskStatus.PENDING
	hours_spent: float = 0.0


class ProductivityReport(BaseModel):
	total_tasks: int
	completed_tasks: int
	total_hours_spent: float
	completion_rate: float


class TaskLogResponse(BaseModel):
	task_id: int
	message: str


class TaskCompletionMetrics(BaseModel):
	total_tasks: int
	completed_tasks: int
	pending_tasks: int
	in_progress_tasks: int
	completion_rate: float
