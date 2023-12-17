import {LoanDto} from "./loan-dto";

export interface LoanListDto {
  items: LoanDto[],
  totalCount: number
}
