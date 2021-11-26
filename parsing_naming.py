import services
import enchant
def parsing(source,parser):
    l = [0]
    li = []

    def parseNode(root):
        if (len(root.children) == 0):
            return
        else:
            for i in root.children:
                if (i.type == 'identifier'):
                    li.append(i)
                    l[-1] += 1
                parseNode(i)

    tree = parser.parse(bytes(source, "utf8"))

    root_node = tree.root_node
    parseNode(root_node)

    source_code_lines = source.split('\n')

    # sys.stdout = open('output', 'w')
    print("no of identifiers in the source code: {}".format(l[-1]))
    print("List of all identifiers with their locations")

    identifiers = []
    for node in li:
        identifier = source_code_lines[node.start_point[0]][node.start_point[1]:node.end_point[1]]
        if not services.check_builtIn(identifier):
            print(identifier, end=' ')
            Line_No = node.start_point[0] + 1
            Col_No = node.start_point[1] + 1
            print(" : Line No: {}, Col No: {} ".format(Line_No, Col_No))
            identifiers.append((identifier, Line_No, Col_No))

    return identifiers


def naming(identifiers):
    short_id_exp = ['c', 'd', 'e', 'g', 'i', 'in', 'inOut', 'j', 'k', 'm', 'n', 'o', 'out', 't', 'x', 'y', 'z']
    d = enchant.Dict("en_US")

    for id in identifiers:
        tog = False
        tog1 = False
        tog2 = False
        if id[0][0] == '_' or id[0][-1] == '_':
            print("Identifier - {} External Underscores at Line no {}, Col no {}".format(id[0], id[1], id[2]))
            tog1 = True
        if '__' in id[0]:
            print("Identifier - {} Consecutive Underscores at Line no {}, Col no {}".format(id[0], id[1], id[2]))
            tog2 = True
        if ('_' in id[0] or any(e.isupper() for e in id[0])) and not tog1 and not tog2:
            if '_' in id[0]:
                w = id[0].split('_')
                count = 0
                for word in w:
                    if services.checkNum(word):
                        count += 1
                if len(id[0]) > 20:
                    print("Identifier -{} is a Long Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if len(w) > 4:
                    print("Identifier -{} has Excessive Words at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if count == len(w):
                    print("Identifier -{} is a Numeric Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                    tog = True
            if any(e.isupper() for e in id[0]) and not '_' in id[0]:
                w = services.words(id[0])
                count = 0
                for word in w:
                    if services.checkNum(word):
                        count += 1
                if len(id[0]) > 20:
                    print("Identifier -{} is a Long Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if len(w) > 4 and any(services.checkNum(e) for e in w):
                    print("Identifier -{} has Excessive Words at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if count == len(w):
                    print("Identifier -{} is a Numeric Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                    tog = True
        if (not d.check(id[0]) or id[0] not in short_id_exp) and not tog and not tog1 and not tog2:
            if '_' in id[0]:
                words2 = id[0].split('_')
                words2 = ''.join(words2)
                w = services.words(words2)
                for word in w:
                    if not d.check(word):
                        print(
                            "Identifier - {} is not a dictionary word or Capitalisation Anamoly at Line no {}, Col no {}".format(
                                id[0], id[1], id[2]))
                        break
                if len(id[0]) > 20:
                    print("Identifier -{} is a Long Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if len(w) > 4:
                    print("Identifier -{} has Excessive Words at Line no {}, Col no {}".format(id[0], id[1], id[2]))
            else:
                w = services.words(id[0])
                w1 = []
                for word in w:
                    if len(word) > 1:
                        w1.append(word)

                for word in w1:
                    if not d.check(word):
                        print(
                            "Identifier - {} is not a dictionary word or Capitalisation Anamoly at Line no {}, Col no {}".format(
                                id[0], id[1], id[2]))
                        break
                if len(id[0]) > 20:
                    print("Identifier -{} is a Long Identifier at Line no {}, Col no {}".format(id[0], id[1], id[2]))
                if len(w1) > 4:
                    print("Identifier -{} has Excessive Words at Line no {}, Col no {}".format(id[0], id[1], id[2]))
        if len(id[0]) < 8 and id[0] not in short_id_exp and d.check(id[0]):
            print("Identifier - {} Short Identifier name at Line no {}, Col no {}".format(id[0], id[1], id[2]))

