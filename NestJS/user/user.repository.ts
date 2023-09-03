//import { User } from "src/auth/user.entity";
import { EntityRepository, Repository } from "typeorm";
import { UserStatus } from "./user-status.enum";
import { User } from "./user.entity";
import { CreateUserDto } from "./dto/create-user.dto";

@EntityRepository(User)
export class UserRepository extends Repository<User> {

    async createUser(createUserDto: CreateUserDto, user: User) : Promise<User> {
        const {username, profileurl} = createUserDto;

        const user = this.create({ 
            title, 
            description,
            status: UserStatus.PUBLIC,
            user
        })

        try {
            await this.save(user);
        } catch (error) {
            if (error.code == '23505')
                throw new ConflictException('Existing username');
            else
                throw new InternalServerErrorException();
        }
        return user;
    }
}
