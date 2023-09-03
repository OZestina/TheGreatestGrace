import { User } from "src/auth/user.entity";
import { BaseEntity, Column, Entity, ManyToOne, PrimaryGeneratedColumn } from "typeorm";
import { UserStatus } from "./user-status.enum";

@Entity()
@Unique(['username'])
export class User extends BaseEntity {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    username: string;

    @Column()
    profileurl: string;

    @Column()
    status: UserStatus;

    // @ManyToOne(type => User, user => user.boards, { eager: false })
    // user: User;
}
