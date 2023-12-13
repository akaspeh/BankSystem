import {TransactionDto} from "./transaction-dto";

export interface TransactionListDto {
  items: TransactionDto[],
  totalCount: number
}
