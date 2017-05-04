CC=gcc
OBJECTS=template.o
TARGET=template

$(TARGET): $(OBJECTS)
	$(CC) -o $@ $^

%.o: %.c
	$(CC) -c $(SYMBOLS) $<

.PHONY: clean

clean:
	rm -f $(TARGET) *.o
