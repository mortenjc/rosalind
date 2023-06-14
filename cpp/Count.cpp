
#include <fstream>
#include <map>
#include <cmath>
#include <cstdlib>
#include <string>
#include <ToolBox.h>

std::string readfile(std::string filename) {
  std::ifstream t(filename);
  std::string str((std::istreambuf_iterator<char>(t)),
                   std::istreambuf_iterator<char>());
   return str;
}

void Rosa1(std::string sequence) {
    std::map<char, uint32_t> counts;
    counts['A'] = 0;
    counts['C'] = 0;
    counts['G'] = 0;
    counts['T'] = 0;
    for (int i = 0; i < sequence.size(); i++) {
      counts[sequence[i]]++;
    }
    printf("%d %d %d %d\n", counts['A'], counts['C'], counts['G'],counts['T']);
}

void Rosa2(std::string sequence) {
    for (int i = 0; i < sequence.size(); i++) {
      if (sequence[i] == 'T')
        sequence[i] = 'U';
    }
    printf("%s\n", sequence.c_str());
}

void Rosa3(std::string sequence) {
  std::map<char, char> subst;
  subst['A'] = 'T';
  subst['T'] = 'A';
  subst['C'] = 'G';
  subst['G'] = 'C';
  std::string result = sequence;
  for (int i = 0; i < sequence.size() - 1; i++) {
      //printf("i %d, result %c, subst %c \n", i, result[i], subst[sequence[i]]);
      result[sequence.size() - 2 - i] = subst[sequence[i]];
  }
  printf("%s\n", result.c_str());
}

uint64_t Rosa4(uint8_t n, uint8_t k) {
  if (n < 3)
    return 1;
  else
    return k * Rosa4(n - 2, k) + Rosa4(n - 1, k);
}

// Computing GC Content
void Rosa4(std::string filename) {
  ToolBox tb;
  auto fasta = tb.fastaLoadFile(filename);
  double maxContent{0.0};
  std::string name;
  struct ToolBox::Fasta * fp;

  for (auto f : fasta) {
    auto content = 100.0 * f.numOfGC / f.numNucleotides;

    if ( content - maxContent > 0.001) {
      printf("Higher!\n");
      name = f.name;
      maxContent = content;
    }
    printf("%s\n", f.name.c_str());
    printf("nuces %u, content %f\n", f.numNucleotides, maxContent);
  }
  printf("%s\n", name.c_str());
  printf("%f\n", maxContent);
}

void Rosa5(std::string name) {
  ToolBox tb;
  auto input = tb.loadFile(name);
  auto res = tb.proteinString(input);
  printf("%s\n", res.c_str());
}

void Rosa6(std::string name) {
  ToolBox tb;
  auto input = tb.loadFile(name);
  auto res = tb.weight(input);
  printf("%.3lf\n", res);
}


int main(int argc, char * argv[]) {
  if (argc != 3) {
    printf("Usage: rosa number filename\n");
    return 0;
  }
  int exercise = atoi(argv[1]);
  auto input = readfile(argv[2]);
  std::string name = argv[2];
  if (input.size() == 0) {
    printf("Empty input - does file exist?\n");
    return 0;
  }

  switch (exercise) {
    case 1:
      Rosa1(input);
    break;
    case 2:
      Rosa2(input);
    break;
    case 3:
      Rosa3(input);
    break;
    case 4:
      Rosa4(name);
    break;
    case 5:
      Rosa5(name);
    break;
    case 6:
      Rosa6(name);
    break;
    default:
      printf("Exercise %d is not implemented\n", exercise);
    break;
  }


  return 0;
}
