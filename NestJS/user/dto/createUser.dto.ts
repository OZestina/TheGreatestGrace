import { IsNotEmpty } from "class-validator";

export class CreateUserDto {
    @IsNotEmpty()
    username: string;

    profileurl: string;

    @IsNotEmpty()
    require2fa: boolean;
}
