
CFLAGS= --std=c++11 -I/usr/local/include -I.

all:
	g++ $(CFLAGS) Count.cpp ToolBox.cpp -o Count

runtest:
	g++ $(CFLAGS) ToolBox.cpp ToolBoxTest.cpp -o ToolBoxTest -lgtest
	./ToolBoxTest

clean:
	rm -f Count ToolBoxTest
