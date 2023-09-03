import { Body, Controller, Delete, Get, Logger, Param, ParseIntPipe, Patch, Post, UseGuards, UsePipes, ValidationPipe } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';
import { GetUser } from 'src/auth/get-user.decorator';
//import { User } from 'src/auth/user.entity';
import { UserStatus } from './user-status.enum';
import { User } from './user.entity';
import { UserService } from './user.service';
import { CreateUserDto } from './dto/create-user.dto';
import { UserStatusValidationPipe } from './pipes/user-status-validation.pipe';

@Controller('user')
@UseGuards(AuthGuard())
export class UserController {
    private logger = new Logger('User');
    constructor(private userService: UserService) { }

    // @Get('/')
    // getAllUser(): User[] {
    //     return this.userService.getAllUser();
    // }

    @Get()
    getAllUser(
        @GetUser() user: User
    ): Promise<User[]> {
        this.logger.verbose(`User ${user.username} trying to get all user`);
        return this.userService.getAllUser(user);
    }

    // @Post()
    // @UsePipes(ValidationPipe)
    // createUser(
    //     @Body() createUserDto: CreateUserDto
    // ): User {
    //     return this.userService.createUser(createUserDto);
    // }

    @Post()
    @UsePipes(ValidationPipe)
    createUser(@Body() createUserDto: CreateUserDto,
    @GetUser() user:User): Promise<User> {
        this.logger.verbose(`User ${user.username} creating a new user. 
        Payload: ${JSON.stringify(createUserDto)} `)
        return this.userService.createUser(createUserDto, user);
    }

    @Get('/:id')
    getUserById(@Param('id') id: number): Promise<User> {
        return this.userService.getUserById(id);
    }

    // @Get('/:id')
    // getUserById(@Param('id') id: string): User {
    //     return this.userService.getUserById(id)
    // }

    @Delete('/:id')
    deleteUser(@Param('id', ParseIntPipe) id,
    @GetUser() user:User
    ): Promise<void> {
        return this.userService.deleteUser(id, user);
    }

    // @Delete('/:id')
    // deleteUser(@Param('id') id: string): void {
    //     this.userService.deleteUser(id);
    // }
    
    @Patch('/:id/status')
    updateUserStatus(
        @Param('id', ParseIntPipe) id: number,
        @Body('status', UserStatusValidationPipe) status: UserStatus
    ) {
        return this.userService.updateUserStatus(id, status);
    }


    // @Patch('/:id/status')
    // updateUserStatus(
    //     @Param('id') id: string,
    //     @Body('status', UserStatusValidationPipe) status: UserStatus
    // ) {
    //     return this.userService.updateUserStatus(id, status);
    // }

}
