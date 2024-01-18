import simpleLanguageModel
import file_io
import sys


if '-i' in sys.argv and len(sys.argv) >= 3:
    file_name_idx = sys.argv.index('-i') + 1
    file_content = file_io.getFileContent(sys.argv[file_name_idx])
    my_vocab_dict = simpleLanguageModel.getPairFrequencies(file_content)
    my_random_sentence = simpleLanguageModel.generateSentence(my_vocab_dict)
    print(my_random_sentence)

# Write the generated sentence to output file
if '-o' in sys.argv and my_random_sentence is not None:
    file_name_idx = sys.argv.index('-o') + 1
    file_io.writeToFile(sys.argv[file_name_idx], my_random_sentence)