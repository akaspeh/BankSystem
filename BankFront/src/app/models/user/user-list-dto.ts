import {UserDto} from "./user-dto";

export interface UserListDto {
  items: UserDto[],
  totalCount: number
}
