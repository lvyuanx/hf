declare interface IEditSetpSort {
  order_type: number | string;
  notes: string;
}

declare interface IStepBase {
  id: number | string;
  name: string;
  notes: string;
  isCheck?: boolean;
  is_skip: boolean;
}

declare interface IStepSort {
  id: number | string;
  name: string;
  step_base: number | string;
  parent_step_id?: number | string;
  child_step_id?: number | string;
  is_skip: boolean;
}
