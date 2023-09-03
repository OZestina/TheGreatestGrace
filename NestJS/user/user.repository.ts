//import { User } from "src/auth/user.entity";
import { EntityRepository, Repository } from "typeorm";
import { UserStatus } from "./user-status.enum";
import { User } from "./user.entity";
import { CreateUserDto } from "./dto/create-user.dto";

@EntityRepository(User)
export class UserRepository extends Repository<User> {

    async createUser(createUserDto: CreateUserDto, user: User) : Promise<User> {
        const {title, description} = createUserDto;

        const user = this.create({ 
            title, 
            description,
            status: UserStatus.PUBLIC,
            user
        })

        await this.save(user);
        return user;
    }
}
