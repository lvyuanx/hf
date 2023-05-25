export interface OrderBase {
  id: number;
  order_code: string;
  order_type: number;
  model_base: number;
  model_base_name: string;
  order_product: string;
  notes: string;
}

export interface OrderList {
  customer: number | string;
  id: number | string;
  order_base: number | string;
  order_technology: string;
}

export interface OrderDetail {
  id?: number | string;
  color: string;
  order_number: number;
  order_price: number;
  order_total_price?: number;
  order_list_id?: number | string;
  notes?: string;
  temp_id?: number | string;
}


export interface OrderType {
  id: number | string;
  name: string;
}
