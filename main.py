from tree_sitter import Language, Parser
import ImportFromGit
import sys
from parsing_naming import parsing, naming

Language.build_library(
  # Store the library in the `build` directory
  'build/my-languages.so',

  # Include one or more languages
  [
    'vendor/tree-sitter-javascript',
    'vendor/tree-sitter-python',
    'vendor/tree-sitter-go',
    'vendor/tree-sitter-ruby',

  ]
)

PY_LANGUAGE = Language('build/my-languages.so', 'python')
GO_LANGUAGE = Language('build/my-languages.so', 'go')
JS_LANGUAGE = Language('build/my-languages.so', 'javascript')
RUBY_LANGUAGE=Language('build/my-languages.so', 'ruby')
py_parser = Parser()
py_parser.set_language(PY_LANGUAGE)


go_parser = Parser()
go_parser.set_language(GO_LANGUAGE)

js_parser = Parser()
js_parser.set_language(JS_LANGUAGE)

ruby_parser = Parser()
ruby_parser.set_language(RUBY_LANGUAGE)

try:
    py_codes,go_codes,js_codes,ruby_codes,py_programs,go_programs,js_programs,ruby_programs=ImportFromGit.retrieve_codes(sys.argv[1])



    sys.stdout = open(sys.argv[4], 'w')

    if sys.argv[2]=='.py' and sys.argv[3].lower()=='python':
        ids2=[]
        for i in range(len(py_codes)):
            print('\n')
            print("output1 for program: {}".format(py_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            ids2.append(parsing(py_codes[i],py_parser))


    elif sys.argv[2]=='.go' and sys.argv[3].lower()=='go':
        ids=[]
        for i in range(len(go_codes)):
            print('\n')
            print("output1 for program: {}".format(go_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            ids.append(parsing(go_codes[i],go_parser))


    elif sys.argv[2]=='.js' and sys.argv[3].lower()=='javascript':
        ids3=[]
        for i in range(len(js_codes)):
            print('\n')
            print("output1 for program: {}".format(js_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            ids3.append(parsing(js_codes[i],js_parser))

    elif sys.argv[2]=='.rb' and sys.argv[3].lower()=='ruby':
        ids4=[]
        for i in range(len(ruby_codes)):
            print('\n')
            print("output1 for program: {}".format(ruby_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            ids4.append(parsing(ruby_codes[i],ruby_parser))

    else:
        print("Invalid input, make sure that file extension belongs to the name of the programming language you mentioned !")


    sys.stdout.close()

    sys.stdout = open(sys.argv[5], 'w')
    if sys.argv[2]=='.py' and sys.argv[3].lower()=='python':
        for i in range(len(py_codes)):
            print('\n')
            print("output2 for program: {}".format(py_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            naming(ids2[i])
    elif sys.argv[2]=='.go' and sys.argv[3].lower()=='go':
        for i in range(len(go_codes)):
            print('\n')
            print("output2 for program: {}".format(go_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            naming(ids[i])
    elif sys.argv[2]=='.js' and sys.argv[3].lower()=='javascript':
        for i in range(len(js_codes)):
            print('\n')
            print("output2 for program: {}".format(js_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            naming(ids3[i])

    elif sys.argv[2]=='.rb' and sys.argv[3].lower()=='ruby':
        for i in range(len(ruby_codes)):
            print('\n')
            print("output2 for program: {}".format(ruby_programs[i]))
            print('--------------------------------------------------------------------------------------------')

            naming(ids4[i])

    else:
        print("Invalid input, make sure that file extension belongs to the name of the programming language you mentioned !")


    sys.stdout.close()
except:
    print("Invalid Input")
    print(" Sample Input format:")
    print("python main.py https://github.com/Harsha2871/SdAllCodes.git .py python output1.txt output2.txt")

