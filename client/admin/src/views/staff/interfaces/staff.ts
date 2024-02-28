export interface StaffBase extends User {
  staff_code: string;
  phone_number?: string;
  avatar: string | File;
  notes?: string;
  role_lst: string[];
}

export interface User {
  fullname: string; // 真实姓名
}
