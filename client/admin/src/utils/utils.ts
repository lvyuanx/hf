/**
 * 判断变量是否为空
 * @param value 任意类型变量
 * @returns 是否为空
 */
export function isEmpty(value:any) {
  if (value === null || value === undefined) {
    return true;
  }
  if (typeof value === "string" && value.trim().length === 0) {
    return true;
  }
  if (Array.isArray(value) && value.length === 0) {
    return true;
  }
  if (typeof value === "object" && Object.keys(value).length === 0) {
    return true;
  }
  return false;
}
