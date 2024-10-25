from plagiarismchecker.algorithm import ConsineSim
from googleapiclient.discovery import build



# searchEngine_API = 'AIzaSyAoEYif8sqEYvj1P6vYLw6CGMrQbDMmaq8' 
searchEngine_API = 'AIzaSyCUYy9AtdMUddiNA0gOcsGPQcE372ytyCw'
#searchEngine_API = 'AIzaSyAQYLRBBeDQNxADPQtUnApntz78-urWEZI'
# searchEngine_API = 'AIzaSyCAeR7_6TTKzoJmSwmOuHZvKcVg_lhqvCc'

# searchEngine_API = 'AIzaSyB-htAtka2OIP-F0NSL7EaCaeRjMH1bhRA'
searchEngine_Id = '671ed2d46502e4ed2'

# searchEngine_Id = '758ad3e78879f0e08'
# searchEngine_API = 'AIzaSyBv8-iI-_O4unTkaskqrhFpvKti14lPTcE'


# searchEngine_Id = '37cf5730519084601'
# searchEngine_API = 'AIzaSyAAD_ZcCmIbaSquTQvCZV2nFrlo4mdzByU'


# 8.5.23 11:30 am
# searchEngine_Id='11f6ecf16b14b4df1'
# searchEngine_API='AIzaSyA7ontrSoOWnBd-WAxzrmqmXyhpWqfKi_c'

# searchEngine_Id = '214819438644f41af'
# searchEngine_API = 'AIzaSyDgUCSQFmLPF36pv1gImNPxmsibAOZJr94'

# searchEngine_API='AIzaSyACDSfEJfk3Tdsb57_iPVdLKJb07lc5yN4'
# searchEngine_Id = '671ed2d46502e4ed2'



# searchEngine_API='AIzaSyAFIMA7CbeBh1neb6QwHcvpVFAIEAvXL_U'
# searchEngine_Id ='40d57d588efd04b9a'

text = str
def searchWeb(text, output, c):
    text = text
    # print(text)
    try:
        resource = build("customsearch", 'v1',
                         developerKey=searchEngine_API).cse()
        result = resource.list(q=text, cx=searchEngine_Id).execute()
        searchInfo = result['searchInformation']

        print("\n This is the Search Info Result \n")
        
        print(result)

        if(int(searchInfo['totalResults']) > 0):
            maxSim = 0
            itemLink = ''
            numList = len(result['items']) 
            if numList >= 5:
                numList = 5
            for i in range(0, numList):
                item = result['items'][i]
                content = item['snippet']
                simValue = ConsineSim.cosineSim(text, content)
                if simValue > maxSim:
                    maxSim = simValue
                    itemLink = item['link']
                if item['link'] in output:
                    itemLink = item['link']
                    break
            if itemLink in output:
                print('if', maxSim)
                output[itemLink] = output[itemLink] + 1
                c[itemLink] = ((c[itemLink] *
                                (output[itemLink]-1) + maxSim)/(output[itemLink]))
            else:
                print('else', maxSim)
                print("\n TEXT:", text)
                print("\n ITEM Link:",itemLink)
                output[itemLink] = 1
                c[itemLink] = maxSim
    except Exception as e:
        print("TEXT:\t",text)
        print(e)
        print('error')
        return output, c, 1
    return output, c, 0
