export interface TransactionCreationDto {
  userIdSender: number
  amount: number
  userIdReceiver: number
  description: string
}
