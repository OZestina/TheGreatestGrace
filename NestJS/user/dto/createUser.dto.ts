import { IsNotEmpty } from "class-validator";

export class CreateUserDto {
    @IsNotEmpty()
    @IsString()
    @MinLength(4)
    @MaxLenght(10)
    username: string;

    @IsString()
    @Matches(정규식, {
        message: 'file name not valid'
    })
    profileurl: string;

    @IsNotEmpty()
    @IsBoolean()
    require2fa: boolean;
}
