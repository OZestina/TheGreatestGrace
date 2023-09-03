import { ArgumentMetadata, BadRequestException, PipeTransform } from "@nestjs/common";
import { UserStatus } from "../user-status.enum";

export class UserStatusValidationPipe implements PipeTransform {
    readonly StatusOptions = [
        UserStatus.PRIVATE,
        UserStatus.PUBLIC
    ]

    transform(value: any, metadata: ArgumentMetadata){
        value = value.toUpperCase();
        console.log(metadata);
      
        if(!this.isStatusValid(value)) {
            throw new BadRequestException(`${value} isn't in the status options`);
        }

        return value;
    }

    private isStatusValid(status: any) {
        const index = this.StatusOptions.indexOf(status);
        return index !== -1
    }

}
