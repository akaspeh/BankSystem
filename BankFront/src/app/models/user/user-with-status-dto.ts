import {UserDto} from "./user-dto";

export interface UserWithStatusDto {
  userDto: UserDto
  status: string
}
