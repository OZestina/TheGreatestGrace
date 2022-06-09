CC		= gcc
CFLAGS	= -Wall -Wextra -Werror
NAME	= do-op
SRCS	= src/*.c
HEADER	= includes

all:	$(NAME)

$(NAME):	$(SRCS)
	$(CC) $(CFLAGS) -o $@ $(SRCS) -I $(HEADER)

clean:
	rm -f $(NAME)

re:	clean all

$(V).SILENT:
