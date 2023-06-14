
#include <gtest/gtest.h>
#include <cmath>
#include <ToolBox.h>

class ToolBoxTest : public ::testing::Test {
 protected:
   ToolBox tb;
  //void SetUp() overide { }

  // void TearDown() override {}
};

TEST_F(ToolBoxTest, TrimString) {
  std::string test0 = "ACTG";
  std::string test1 = "ACTG\n";

  auto res = tb.trim(test0);
  ASSERT_TRUE(res.size() == test0.size());

  int oldsize = test1.size();
  res = tb.trim(test1);
  ASSERT_TRUE(res.size() == oldsize - 1);

}

TEST_F(ToolBoxTest, ReverseString) {
  std::string test0 = "ABCDEFGH";
  std::string test1 = "ABC";

  auto res = tb.reverse(test0);
  ASSERT_EQ(res, "HGFEDCBA");

  res = tb.reverse(test1);
  ASSERT_EQ(res, "CBA");
}

TEST_F(ToolBoxTest, CountGC) {
  ASSERT_EQ(0, tb.countGC("AAAAAAAA"));
  ASSERT_EQ(2, tb.countGC("ACAAAGAA"));
  ASSERT_EQ(2, tb.countGC("CAATATG"));
}

TEST_F(ToolBoxTest, ProteinString) {
  std::string rna("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA");
  ASSERT_EQ("MAMAPRTEINSTRING", tb.proteinString(rna));
}

TEST_F(ToolBoxTest, ProteinWeight) {
  std::string protein("SKADYEK");
  ASSERT_TRUE( std::abs(821.392 - tb.weight(protein)) < 0.001);
}

TEST_F(ToolBoxTest, ReadFasta) {
  auto fasta = tb.fastaLoadFile("testdata/gccount.fst");
  ASSERT_EQ(fasta.size(), 3);
  double maxContent{0.0};
  struct ToolBox::Fasta * fp;
  for (auto f : fasta) {
    auto content = 100.0 * f.numOfGC / f.numNucleotides;
    if ( content > maxContent) {
      fp = &f;
      maxContent = content;
    }
  }
  ASSERT_EQ(fp->name, "Rosalind_0808");
  ASSERT_TRUE(std::abs(maxContent - 60.919540) < 0.001);
}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
