declare interface IResult<T> {
  code: number,
  msg: string,
  data: T
}

declare interface IPage<T> {
  total: number;
  pageCount: number;
  currentPage: number;
  pageSize: number;
  results: T[]
}

declare interface IPageResult<T> {
  code: number,
  msg?: string,
  data?: IPage<T>
}
