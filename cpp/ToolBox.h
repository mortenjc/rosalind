
#include <vector>
#include <string>
#include <map>

class ToolBox {

public:
  struct Fasta {
    std::string name;
    uint32_t numNucleotides{0};
    uint32_t numOfGC{0};
  };

  std::map<char, double> weights {
    {'A',    71.03711},
    {'C',    103.00919},
    {'D',    115.02694},
    {'E',    129.04259},
    {'F',    147.06841},
    {'G',    57.02146},
    {'H',    137.05891},
    {'I',    113.08406},
    {'K',    128.09496},
    {'L',    113.08406},
    {'M',    131.04049},
    {'N',    114.04293},
    {'P',    97.05276},
    {'Q',    128.05858},
    {'R',    156.10111},
    {'S',    87.03203},
    {'T',    101.04768},
    {'V',    99.06841},
    {'W',    186.07931},
    {'Y',    163.06333}
  };

  std::map<std::string, std::string> proteinmap {
    {"UUU", "F"},    {"CUU", "L"},   {"AUU", "I"},    {"GUU", "V"},
    {"UUC", "F"},    {"CUC", "L"},   {"AUC", "I"},    {"GUC", "V"},
    {"UUA", "L"},    {"CUA", "L"},   {"AUA", "I"},    {"GUA", "V"},
    {"UUG", "L"},    {"CUG", "L"},   {"AUG", "M"},    {"GUG", "V"},
    {"UCU", "S"},    {"CCU", "P"},   {"ACU", "T"},    {"GCU", "A"},
    {"UCC", "S"},    {"CCC", "P"},   {"ACC", "T"},    {"GCC", "A"},
    {"UCA", "S"},    {"CCA", "P"},    {"ACA", "T"},    {"GCA", "A"},
    {"UCG", "S"},    {"CCG", "P"},    {"ACG", "T"},    {"GCG", "A"},
    {"UAU", "Y"},    {"CAU", "H"},    {"AAU", "N"},    {"GAU", "D"},
    {"UAC", "Y"},    {"CAC", "H"},    {"AAC", "N"},    {"GAC", "D"},
    {"UAA", "Stop"}, {"CAA", "Q"},    {"AAA", "K"},    {"GAA", "E"},
    {"UAG", "Stop"}, {"CAG", "Q"},    {"AAG", "K"},    {"GAG", "E"},
    {"UGU", "C"},    {"CGU", "R"},    {"AGU", "S"},    {"GGU", "G"},
    {"UGC", "C"},    {"CGC", "R"},    {"AGC", "S"},    {"GGC", "G"},
    {"UGA", "Stop"}, {"CGA", "R"},    {"AGA", "R"},    {"GGA", "G"},
    {"UGG", "W"},    {"CGG", "R"},    {"AGG", "R"},    {"GGG", "G"}
  };

  uint32_t countGC(std::string input);

  std::string proteinString(std::string rnastring);

  double weight(std::string proteinstring);

  std::string loadFile(std::string filename);

  std::vector<struct Fasta> fastaLoadFile(std::string filename);

  std::string trim(std::string & input);

  std::string reverse(std::string & input);

  uint32_t fastaGetNumDataSets(std::vector<struct Fasta> data) const { return data.size(); }

private:


};
