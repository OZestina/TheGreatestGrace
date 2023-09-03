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
        private boardRepository: UserRepository,
    ) { }

    async getAllUser(
        user: User
    ): Promise<User[]> {
        const query = this.boardRepository.createQueryBuilder('user');

        query.where('user.userId = :userId', { userId: user.id});

        const boards = await query.getMany();

        return boards;
    }

  
    createUser(createUserDto: CreateUserDto, user: User): Promise<User> {
        return this.boardRepository.createUser(createUserDto, user);
    }

    async getUserById(id: number): Promise<User> {
        const found = await this.boardRepository.findOne(id);

        if (!found) {
            throw new NotFoundException(`Can't find User with id ${id}`);
        }

        return found;
    }

    // getUserById(id: string): User {
    //     const found = this.boards.find((user) => user.id === id);

    //     if (!found) {
    //         throw new NotFoundException(`Can't find User with id ${id}`);
    //     }

    //     return found;
    // }

    async deleteUser(id: number, user: User): Promise<void> {
        const result = await this.boardRepository.delete({id, user});

        if (result.affected === 0) {
            throw new NotFoundException(`Can't find User with id ${id}`)
        }
    }

    // deleteUser(id: string): void {
    //     const found = this.getUserById(id);
    //     this.boards = this.boards.filter((user) => user.id !== found.id);
    // }


    async updateUserStatus(id: number, status: UserStatus): Promise<User> {
        const user = await this.getUserById(id);

        user.status = status;
        await this.boardRepository.save(user);

        return user;
    }
    // updateUserStatus(id: string, status: UserStatus): User {
    //     const user = this.getUserById(id);
    //     user.status = status;
    //     return user;
    // }

}
