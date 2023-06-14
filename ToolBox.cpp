

#include <ToolBox.h>
#include <fstream>
#include <string>

std::string ToolBox::loadFile(std::string filename) {
  std::ifstream file(filename);
  std::string result;
  if (file.is_open()) {
    std::string line;
    while (getline(file, line)) {
      result += trim(line);
    }
    file.close();
  }
   return result;
}

std::vector<struct ToolBox::Fasta> ToolBox::fastaLoadFile(std::string filename) {
  std::ifstream file(filename);
  std::vector<struct ToolBox::Fasta> result;

  if (file.is_open()) {
    std::string line;
    ToolBox::Fasta * fp{nullptr};
    while (getline(file, line)) {
      trim(line);

      if (line[0] == '>') {

        // push old data
        if (fp != nullptr) {
              result.push_back(*fp);
        }
        // create new
        fp = new ToolBox::Fasta();
        fp->name = line.substr(1,  std::string::npos);
      } else {
        fp->numNucleotides += line.size();
        fp->numOfGC += countGC(line);
      }
    }
    if (fp != nullptr)
          result.push_back(*fp);
    file.close();
  }
  return result;
}

uint32_t ToolBox::countGC(std::string input) {
  uint32_t gc{0};
  for (int i = 0; i < input.size(); i++) {
    if (input[i] == 'G' or input[i] == 'C')
      gc++;
  }
  return gc;
}

std::string ToolBox::proteinString(std::string rnastring) {
  if (rnastring.size() %3 != 0)
    return " - INVALID RNA -";
  std::string result;

  for (int i = 0; i < rnastring.size(); i += 3) {
    std::string triplet{""};

    triplet += rnastring[i + 0];
    triplet += rnastring[i + 1];
    triplet += rnastring[i + 2];

    std::string pro = ToolBox::proteinmap[triplet];
    if (pro.compare("Stop") == 0) {
      return result;
    }
    result += pro;
  }
  return result;
}

double ToolBox::weight(std::string proteinstring) {
  double sum{0.0};
  for (int i = 0; i < proteinstring.size(); i++) {
    char b = proteinstring[i];
  //  printf("protein %s\n", s.c_str());
    double a = ToolBox::weights[b];
    sum += a;
  }
  return sum;
}

// void fastaCountGC(std::vector<std::string> lines) {
//   for (auto line : lines) {
//
//   }
// }


std::string ToolBox::trim(std::string & input) {
  if (input[input.size() - 1] == '\n') {
    input.resize(input.size() - 1);
  }
  return input;
}

std::string ToolBox::reverse(std::string & input) {
  for (int i = 0; i < input.size()/2; i++) {
    char tmp = input[i];
    int swapwith = input.size() - 1 - i;
    input[i] = input[swapwith];
    input[swapwith] = tmp;
  }
  return input;
}
