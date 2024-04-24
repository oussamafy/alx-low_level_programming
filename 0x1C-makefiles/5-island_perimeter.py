CC = gcc
SRC = main.c holberton.c
OBJ = $(SRC:.c=.o)
NAME = holberton
RM = rm -f
CFLAGS = -Wall -Werror -Wextra -pedantic
all: $(OBJ)
	$(CC) $(OBJ) -o $(NAME)
clean:
	$(RM) *~ $(NAME)
oclean:
	$(RM) $(OBJ)
fclean: clean oclean
re: oclean all
