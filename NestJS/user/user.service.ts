import { Injectable, NotFoundException } from '@nestjs/common';
import { UserStatus } from './user-status.enum';
import { CreateUserDto } from './dto/create-user.dto';
import { UserRepository } from './user.repository';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './user.entity';
import { User } from 'src/auth/user.entity';

@Injectable()
export class UserService {
    constructor(
        @InjectRepository(UserRepository)
        private userRepository: UserRepository,
    ) { }

    async getAllUser(
        user: User
    ): Promise<User[]> {
        const query = this.userRepository.createQueryBuilder('user');

        query.where('user.userId = :userId', { userId: user.id});

        const users = await query.getMany();

        return users;
    }

  
    createUser(createUserDto: CreateUserDto, user: User): Promise<User> {
        return this.userRepository.createUser(createUserDto, user);
    }

    async getUserById(id: number): Promise<User> {
        const found = await this.userRepository.findOne(id);

        if (!found) {
            throw new NotFoundException(`Can't find User with id ${id}`);
        }

        return found;
    }

    async deleteUser(id: number, user: User): Promise<void> {
        const result = await this.userRepository.delete({id, user});

        if (result.affected === 0) {
            throw new NotFoundException(`Can't find User with id ${id}`)
        }
    }


    async updateUserStatus(id: number, status: UserStatus): Promise<User> {
        const user = await this.getUserById(id);

        user.status = status;
        await this.userRepository.save(user);

        return user;
    }
}
