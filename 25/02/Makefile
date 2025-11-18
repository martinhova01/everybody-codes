CC = gcc
CFLAGS = -O3 -fopenmp -Wall -std=c99
TARGET = main

all: $(TARGET)

$(TARGET): main.c
	$(CC) $(CFLAGS) main.c -o $(TARGET)

clean:
	rm -f $(TARGET)