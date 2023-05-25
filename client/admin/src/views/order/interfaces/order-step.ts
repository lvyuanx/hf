export interface StepOrderChangeRecord {
  id: number | string
  is_delete: boolean
  notes: string
  order_type: 2
}

export interface StepBase {
  id: number | string;
  name: string;
  notes: string;
  isCheck?: boolean;
  is_skip: boolean;
}

export interface StepSort {
  id: number | string;
  name: string;
  step_base: number | string;
  parent_step_id?: number | string;
  child_step_id?: number | string;
  is_skip: boolean;
}
