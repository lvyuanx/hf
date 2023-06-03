import { UploadRawFile } from "element-plus";

export interface StaffBase {
  user: User;
  staff_code: string;
  phone_number: string;
  avatar: UploadRawFile | null;
  notes: string;
}

export interface User {
  username: string;
  password: string;
}
