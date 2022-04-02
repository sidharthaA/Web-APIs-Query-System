def isFloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def check(fields, type):
    names1 = ['id', 'title', 'summary', 'rating', 'name', 'label', 'author',
              'description', 'type', 'downloads', 'useCount', 'sampleUrl',
              'downloadUrl', 'dateModified', 'remoteFeed', 'numComments', 'commentsUrl',
              'Tags', 'category', 'protocols', 'serviceEndpoint', 'version', 'wsdl', 'data formats',
              'apigroups', 'example', 'clientInstall', 'authentication', 'ssl', 'readonly', 'VendorApiKits',
              'CommunityApiKits', 'blog', 'forum', 'support', 'accountReq', 'commercial', 'provider', 'managedBy',
              'nonCommercial', 'dataLicensing', 'fees', 'limits', 'terms', 'company', 'updated']

    add = ['dateModified', 'numComments', 'commentsUrl',
           'tags', 'APIs', 'updated']
    names2 = names1[:12] + add
    d = {}
    for i in range(len(fields)):
        if type == 'api':
            if fields[i] == "":
                fields[i] = None
            elif '###' in fields[i]:
                output = []
                sep = fields[i].split('###')
                for j in range(len(sep)):
                    output.append(sep[j])
                fields[i] = output
            elif fields[i].isdigit():
                fields[i] = int(fields[i])
            elif isFloat(fields[i]):
                fields[i] = float(fields[i])

            d[names1[i]] = fields[i]

        else:
            if fields[i] == "":
                fields[i] = None
            elif '###' in fields[i]:
                output = []
                sep = fields[i].split('###')
                for j in range(len(sep)):
                    output.append(sep[j])
                fields[i] = output
            elif '$$$' in fields[i]:
                output = []
                sep = fields[i].split('$$$')
                for j in range(len(sep)):
                    output.append(sep[j])
                fields[i] = output
            elif fields[i].isdigit():
                fields[i] = int(fields[i])
            elif isFloat(fields[i]):
                fields[i] = float(fields[i])

            d[names2[i]] = fields[i]

    return d


def parse(file, type):
    final = []
    for line in file:
        fields = line.split('$#$')
        dic = check(fields, type)
        final.append(dic)
    return final


def main():
    file1 = open('api.txt', 'r', encoding="ISO-8859-1")
    file2 = open('mashup.txt', 'r', encoding="ISO-8859-1")

    api_data = parse(file1, "api")
    mashup_data = parse(file2, "mashup")
    return api_data, mashup_data