#=================================#
# [ OWNER ]
#     CREATOR  : Vladislav Khudash
#     AGE      : 17
#     LOCATION : Ukraine
#
# [ PINFO ]
#     DATE     : 06.05.2026
#     PROJECT  : PYTHON-PACKER
#     PLATFORM : ANY
#=================================#




from os.path import (
    isfile, 
    realpath,
    split as splitp, 
    join  as joinp
)
from mmap    import mmap,   ACCESS_READ
from sys     import argv,   version_info
from secrets import choice, randbelow,   token_bytes
from gzip    import compress  as gzip
from pickle  import dumps     as pickle
from base64  import b85encode as base64
from codecs  import encode    as codecs
from zlib    import compress  as zlib
from lzma    import compress  as lzma, FILTER_LZMA1, FORMAT_RAW




__file__ = realpath(argv[0])


ENCODING = 'UTF-8'
BASIS    = (bin, oct, int, hex)
ALPHABET = (
    '_'
    '0123456789'
    'αβγδεζηθικλμνξπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΠΡΣΤΥΦΧΨΩ'
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюяґєіїАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯҐЄІЇ'
    'あいうえおかきくけこ'
    'جهدخذارزسشصضطظعغفقكلمنهوي'
    'アイウエオカキクケコサシスセソ'
    'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ'
    'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ'
    'अआइईउऊऋऌएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह'
    'ᚠᚢthᚨᚱᚲᚷᚹᚺᚻᚼᚽᚾᚿᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟᛠᛡᛢᛣᛤᛥᛦᛧᛨᛩᛪ'
    '维度空間術式隠密虚空混沌断絶境界零極幻影幽冥封印禁忌呪縛乖離鍵扉深淵監視'
    'ሀሁሂሃሄህሆሇለሉሊላሌልሎሏሐሑሒሓሔሕሖሗመሙሚማሜምሞሟሠሡሢሣሤሥሦሧረሩሪራሬርሮሯ'
    'ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՒՓՔՕՖաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցւփքօֆ'
    'ᐁᐂᐃᐄᐅᐆᐇᐈᐉᐊᐋᐌᐍᐎᐏᐐᐑᐒᐓᐔᐕᐖᐗᐘᐙᐚᐛᐜᐝᐞᐟᐠᐡᐢᐣᐤᐥᐦᐧᐨᐩᐪᐫᐬᐭᐮᐯᐰᐱᐲᐳᐴᐵᐶᐷᐸᐹᐺᐻᐼᐽᐾᐿᑀᑁᑂᑃᑄᑅᑆᑇᑈᑉᑊᑋᑌᑍᑎᑏᑐᑑᑒᑓᑔᑕᑖᑗᑘᑙᑚᑛᑜᑝᑞᑟᑠᑡᑢᑣᑤᑥᑦᑧᑨᑩᑪᑫᑬᑭᑮᑯᑰᑱᑲᑳᑴᑵᑶᑷᑸᑹᑺᑻᑼᑽᑾᑿ'
)


NONE = (
    '''((None)and((lambda:None)())and(([]or(None)))and(({}or(None)))and((set()or(None)))and([].append(0)or(None))and(((0)if(False)else(None)))and((lambda x=None:x)())and((not(True))and(None))and((1>2)and(None))and((0==1)and(None))and(([]and(None)))and(({}and(None)))and((sum([])or(None)))and(([(i)for(i)in(range(0))]or(None)))and(((lambda x:[].pop())if(False)else(None))())and(((None)if(True)else(0)))and((len([])==0)and(None))and(((0)in[])and(None))and(((False)or(None)))and((len([0]*0)and(None)))and(((set())&(set())or(None)))and(({}|{}or(None)))and(((0)and(None)))and((not(1))and(None))and((lambda x:(x)and(None))(0))and(([]is not[0])and(None))and(({}is not{'a':1})and(None))and(((0)if(1>2)else(None)))and(([]or{}or(None)))and((sum([0]*0)or(None)))and((len([(n)for(n)in(range(0,1))if(False)])or(None)))and((lambda y:(None)if(y)else(0))(False))and((not([]or{})or{1,2,3}))and((()or(None)))and((lambda x=None:x)()or(None))and((set()-set()or(None)))and(((666)in(set())and(None)))and(([]+[]or(None)))and(({}and[])))''',
    '''([].append(0)or(None))''',
    '''(((0)if(False)else(None))and((lambda x=None:x)()))''',
    '''((not(not(False)))or(None)and(1>2))''',
    '''(not(0==1)and(not((None)is not(None)))and([0]and(None)))''',
    '''(({None}and(None))and(sum([])or(None)))''',
    '''(([(j)for(j)in(range(0))]or(None))and((lambda x:([].pop())if(False)else('_start()'))()))''',
    '''(((None)if((3%2==1//1==1)*0==0)else('main()'))and((len([])==0)and(None)))''',
    '''(((0**0*0*0**0)in[0])and(None)and((False)or(None)))''',
    '''((len([0]*1)and(None))and(((set())&(set())or(None))))''',
    '''(({}|{}or(None))and((0)and(False))and(not(1))and(None))''',
    '''((lambda z:(z)or(None))(None)and([]is not[0])and(True))''',
    '''(({}is not{'a':1})and(len([[1]][0]))and((0)if(1*2>2)else(None)))''',
    '''(([]or{}or((0,0)))and(sum([0]*0)or(None)))''',
    '''((len([(v)for(v)in(range(0,1))if(3%2==1)])or(666%3==3<<1))and((lambda x:(None)if(x)else(0))(333%2==13%2==2>>1>0)))''',
    '''((not([]or{})and(None))and(()or()))''',
    '''((lambda x=None:x)()or(1)and((set()-set())or(None)))''',
    '''(((0)in(set([0]))and(True))and([]+[]or(None)))''',
    '''(({}and[]or(float('inf')>(0)))and((len([(j)for(j)in(range(666,667))])==1)and((float('-inf')<(1991%1991))and(None))))''',
    '''((lambda _:[(__)for(__)in(range(0))]or(None))(...)and(([]or(None))and(False)or(None)))'''
)

TRUE = (
    '''((1<<0==1)and(2**0==1)and(3%2==1)and(10//10==1)and(5-4==1)and(len([0])==1)and(len({42})==1)and(set([1])&set([1])=={1})and((3*1==3))and((2**3-7==1))and((lambda x:x^x)(42)==0)and((ord('B')-ord('A'))==1)and((not[]==False))and(([]==[]))and(({}=={}))and((1+2-2==1))and((len('abc')-2==1))and(((10%3!=0)or(1)))and((3//3==1))and((bool([1])==True))and((bool([])==False))and((0==False))and((1!=0))and((~(-1)==0))and((5&1==1))and((5|2==7))and((5^2==7))and((4>>2<2))and((1<<1>>1==1))and((3*0+1==1))and((len('x'*3)//3==1))and((len('x'[0:1])==1))and((ord('Z')-ord('A')==25))and((('a')in('abc')))and((('z')not in('abc')))and((int(True)==1))and((int(2>1)==1))and((int(2>=1)==1))and((int(1>=1)==1))and((not(None)==True))and((len([(i)for(i)in(range(1))])==1))and((sum([1,0])==1))and((sum([1]*1)//1==1))and((sum({1,1})==1))and((len('!!')-1==1))and((len('aa')//2==1))and((10-9==1))and((4//2==2))and((6-5==1))and((2**1-1==1))and((len({(i)for(i)in(range(5))}&{2,3})==2))and(((3%3==0)or(1)))and((len([0]*1)==1))and((len({'a':1})==1)))''',
    '''((lambda x:x^x)(42)==0)and((ord('B')-ord('A'))==1)and((not[]==False))and(([]==[]))and(({}=={}))and((1+2-2==1))and((len('abc')-2==1))and(((10%3!=0)or(1)))''',
    '''((3//3==1)and(bool([1])==True)and(bool([])==False)and(0==False)and(1!=0)and((~(-1)==0))and((5&1==1))and((5|2==7)))''',
    '''((5^2==7)and(4>>2<2)and(1<<1>>1==1)and(3*0+1==1)and(len('x'*3)//3==1)and(len('x'[0:1])==1)and((ord('Z')-ord('A')==25)))''',
    '''((('a')in('abc'))and(('z')not in('abc'))and((int(True)==1))and((int(2>1)==1))and((int(2>=1)==1))and((int(1>=1)==1)))''',
    '''((not(None)==True)and(len([int([(j)for(j)in(range(666,667,666))]==[666])])==1)and((sum([1,0])==1))and((sum([1]*1)//1==1))and((sum({1,1})==1)))''',
    '''((len('!!')-1==1)and((len('aa')//2==1))and((10-9==1))and((4//2==2))and((6-5==1))and((2**1-1==1)))''',
    '''((len({(i)for(i)in(range(5))}&{2,3})==2)and(((3%3==0)or(1)))and((len([0]*1)==1))and((len({'a':1})==1)))''',
    '''((((1)in[1]))and(((2)not in[3]))and(((3)in(set([3,4]))))and(((4)not in(set([1,2])))))''',
    '''(((0)!=(None))or(1)and(([]is not[0]))and(({}is not{'a':1}))and((('x')in('xyz'))))''',
    '''((len([(sex)for(sex)in(range(2))])==2)and((sum([1,1])==2))and((2**1==2))and((3%2==1)))''',
    '''((bool([0,1])==True)and((not[]==False))and((1!=0))and((~(-1)==0))and((5&1==1)))''',
    '''((len("hello"[1:4])==3)and((3*1==3))and((2**2-3==1))and((10//5==2)))''',
    '''((sum([(y)for(y)in(range(3))])==3)and((len({1,2,3}&{2,3})==2))and((("c++")in[1,2,3,'c++'])))''',
    '''((lambda x:x|0)(5)==5)and((1<<2>>1==2))and((4>>1<<1==4))and((1^0==1))''',
    '''((len([1]*1)==1)and((2**0==1))and(((10%10==0)or(1)))and(((3%3==0)or(1))))''',
    '''((('python')in("python"))and(('_')not in('abc'))and((1+0==1))and((2*0+1==1)))''',
    '''((sum([0,0,0,1,0,0])==1)and((len([0]*1)//1==1))and((int(1>=1)==1))and((not[]==False)))''',
    '''((3%2==1)and(((1)in {1,2,1}))and(((0)not in{1}))and(((2)in(1,2,3))))''',
    '''(([(u)for(u)in(range(-3,4))]==[-3,-2,-1,0,1,2,3])and((sum([1]*1)//1==1))and((1*1==1))and((len({'C++/Python'})==1)))'''
)

ELLIPSIS = (
    '''((lambda x:(x)if(x)is(None)else(...))(...))''',
    '''((([].append(0)or{1})and((...)or(2%2==0))))''',
    '''((((0)if(False)else(...))and(lambda y:(y)or(...))(None)))''',
    '''((not([]or{})and((...)not in({...})))or((lambda:...)()))''',
    '''(((sum([0]*0)or(...))if(len([])==0)else(True)))''',
    '''((lambda a,b:((...)if(a>b>-1)else(b)))(True,0))''',
    '''(((...)or(...))if(1>2)else(...))''',
    '''((((0)in[[[0]]])and(...)or(1991%1==0)and(...))or((lambda n:(n)or(None))(False)))''',
    '''((({}or[])or(...)or(()))and((lambda z:((z)or{'c++'})and(...))(None)))''',
    '''(((lambda i:(i)if(i)else(...))(False))or(([]and(...))))''',
    '''((not(None)and(...))or((len([(j)for(j)in(range(0))])or(2**32-1))))''',
    '''((lambda u:((...)if(u)else(0)))(2>>999%2)and(((0)or(...))))''',
    '''(((lambda q=None:(...)if(q)is(None)else(0))((False==True)or(None)))and((...)or(0)))''',
    '''((((0)and(1))or(...))if(len({})==0)else((lambda k:...)(None)))''',
    '''((not(True)and(not(not(True)))or(...))and(([]or(...))and(lambda:...)()))''',
    '''((lambda _:(((_)and(False))or(...)))('_'))''',
    '''((lambda __:((...)if(__)else(1)))((sum([])or(0))==0))''',
    '''(((lambda v:...)(None))and(((0)or(None))if(False)else(...)))''',
    '''(((666%3==0==1)and(...)or(({}or((...)))or(2<<2>>2))))''',
    '''((not(not([]))and(~0==1)or(...))or((lambda w:(w)if(w)else(0))(...)))'''
)


MODULE = (
    '{}=__builtins__.getattr(__builtins__.getattr(__builtins__,{}),{})(__builtins__.getattr(__builtins__,{}),{});'
    'from builtins import bytes as {}, enumerate as {},globals as {},exec as {},compile as {},__import__ as {},getattr as {},int as {};'
    '{}=[{{{}:{}({},{})({}[{}:{}],{}),{}:{}[{}],{}:{}[{}],{}:{}[{}]}}];'
    'from sys import exit as {},gettrace as {};'
    '{}({}[{}],{})({},{});'
    '{}({}(),{})({},\'{}\');'
    'from operator import add as {},sub as {},and_ as {},xor as {},is_ as {},eq as {};'
    '{}=lambda {}:{}({}({}),{})({},{},{},{});'
    '{}({}(),{})({})'
)

INITPYC = (
    'def {}():'
    '{};'
    '{}={}({}({}),{})({}({}({},{})({}({}(),{})({})),({}({}(),{})({}))));{}={};{}={}({}({}),{})();'
    '{}({},{})({})({}({}));'
    '{}={}({},{})({});'
    '{}({}(),{})({}),{}({}(),{})({}),{}({}(),{})({{{}:({}({},{})({}({}({},{})(),{},{},{},{})))}});'
    'return({}({},{}))\n'

    '(({}({}({}(),{})({}),{}))and({}({}(),{}))and({}({}({}(),{})({}),{})))and({}({}()({}({}(),{})({})),{})),'
    '{}({});'
    '__bootstrap({})'
)

INITPYC_ROT = (
    '{}=lambda {}:'
    '{}({}({},{})'
    '({},(({}({}({}({},({}({},{}))),{}),{})for({},{})in({}({}))))),{},{},{},{})'
)

INITPYC_FOR = (
    'for({},{})in({}({})):'
    '{}={};'
    '{}({},{})({}({},{})({}({},{}({}({},{}({},{})),{}))));'
    '{}={}({}({},{}),{})'
)


LZMA_FILTER = ({
    'id'        : FILTER_LZMA1,
    'dict_size' : 4 << 20,   
    'lc'        : 4,
    'lp'        : 0,
    'pb'        : 2
},)

RAW_LZMA_FILTER = memoryview(
    LZMA_FILTER[0]['dict_size'].to_bytes(4, 'little') +
    bytes((
        LZMA_FILTER[0]['lc'], 
        LZMA_FILTER[0]['lp'], 
        LZMA_FILTER[0]['pb']
    ))
)




_start = type('', (), {'__slots__' : ()})
def main(_): pass




def _chr_str(attr, s, d=False):
    return BASIS[randbelow(3)](s) if d else (
        ("f'" + 
            (
                f'{{chr({_chr_str(None, ord("%"), d=True)})}}'
                f'{{chr({_chr_str(None, ord("s"), d=True)})}}'
            ) 
        + f"'*{_chr_str(None, len(s), d=True)}%" + 
            ('(' + 
                ','.join(f'chr({BASIS[randbelow(3)](ord(n))})' for n in s) 
            ) + ')'
        )


            if attr is None else 


        (
            f'{attr[0]}("' +
            ''.join(
                [chr((ord(n) << attr[1]) ^ attr[2]) for n in s]
            ).replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n') 
            + '")'
        )
    )




def name(NaN=ALPHABET.replace('0123456789', '')):
    return f'{choice(NaN)}{"".join( choice(ALPHABET) for _ in range(4 + randbelow(250)) )}'




def enc(hd, key):
    k0, k1 = key

    with mmap(hd, 0, access=ACCESS_READ) as mf:
        sz  = len(mf)
        buf = bytearray(sz)
        ptr = memoryview(buf)


        f = k0

        for i in range(sz):
            n = mf[i]

            x = n ^ (( (k1 + f) + i ) & 0xFF)
            f = (f ^ x) & 0xFF

            ptr[i] = x


    return ptr




def rot_enc(s, k): 
    return memoryview(bytes(( (n + k) ^ (0x55 + i) ) & 0xFF 
                            for (i, n) in enumerate(s)))




def pypack(p):
    KEY     = tuple(token_bytes(2))
    CHR_KEY = (randbelow(6) + 1, randbelow(255))
    ROT_KEY = randbelow(255)


    opath = splitp(p)
    oname = joinp(opath[0], 'packed-' + opath[-1])


    with open(p, 'rb') as f:
        enc_code = enc(f.fileno(), KEY)


    _enc_code_func      = name()
    _enc_code           = memoryview(gzip(enc_code, compresslevel=9))
    _enc_code_signature = _enc_code[:10].hex()
    _enc_code_body      = _enc_code[10:].tobytes()


    _chr_func = name()
    chr_str   = lambda s, d=False: _chr_str(
        (_chr_func, CHR_KEY[0], CHR_KEY[1]), 
        s, d
    )


    (
        _loads,        _pickled_code, _bytes,   _enumerate,
        _globals,      _exec,         _compile, _import,
        _getattr,      _int,          _exit,    _debug,
        _add,          _sub,          _and,     _xor,
        _is,           _eq,           _c,       _pyc,
        _init,         _rot,          _rot_c,   _rot_i,
        _rot_n,        _s,            _f,       _r,
        _i,            _n,            _x,       _marshal,
        _filter_bytes, _filter,       _lzma,    _code,
    ) = (name() for _ in range(36))


    _module = base64(MODULE.format(
        _filter_bytes, 
        chr_str('memoryview'),
        chr_str('__new__'),
        chr_str('memoryview'),
        RAW_LZMA_FILTER.tobytes(),
        _bytes,
        _enumerate, 
        _globals, 
        _exec, 
        _compile,
        _import, 
        _getattr, 
        _int,
        _filter,
        chr_str('dict_size'), 
        _getattr,
        _int,
        chr_str('from_bytes'),
        _filter_bytes, 
        chr_str(0, d=True), 
        chr_str(4, d=True), 
        chr_str('little'),
        chr_str('lc'), 
        _filter_bytes, 
        chr_str(4, d=True),
        chr_str('lp'), 
        _filter_bytes, 
        chr_str(5, d=True),
        chr_str('pb'), 
        _filter_bytes, 
        chr_str(6, d=True),
        _exit, 
        _debug,
        _getattr,
        _filter, 
        chr_str(0, d=True), 
        chr_str('__setitem__'),
        chr_str('id'), 
        chr_str(FILTER_LZMA1, d=True),
        _getattr,
        _globals,
        chr_str('__setitem__'),
        chr_str(_enc_code_func),
        _enc_code_signature,
        _add,
        _sub,
        _and,
        _xor,
        _is,
        _eq,
        _lzma, 
        _c,
        _getattr,
        _import,
        chr_str('lzma'),
        chr_str('decompress'),
        _c,
        chr_str(FORMAT_RAW, d=True), 
        choice(NONE),
        _filter,
        _getattr,
        _globals,
        chr_str('pop'),
        chr_str('main')
    ).encode(ENCODING))


    _for = rot_enc(INITPYC_FOR.format(
        _i,
        _n,
        _enumerate, 
        _s,
        _x,
        _n,
        _getattr,
        _r,
        chr_str('write'),
        _getattr,
        _int,
        chr_str('to_bytes'),
        _xor,
        _x,
        _and,
        _add,
        chr_str(KEY[1], d=True),
        _add,
        _f,
        _i,
        chr_str(0xFF, d=True),
        _f,
        _and,
        _xor,
        _f,
        _x,
        chr_str(0xFF, d=True)
    ).encode(ENCODING), ROT_KEY)


    _rot_code = INITPYC_ROT.format(
        _rot,        
        _rot_c, 
        _compile,      
        _getattr,      
        _bytes,        
        chr_str('__new__'),  
        _bytes,
        _and,
        _sub,
        _xor,
        _rot_n,     
        _add,
        chr_str(0x55, d=True),
        _rot_i,   
        ROT_KEY,       
        chr_str(0xFF, d=True),
        _rot_i,
        _rot_n,
        _enumerate,
        _rot_c,
        chr_str('<...>'),
        chr_str('exec'),
        chr_str(0, d=True),
        choice(TRUE)
    )


    _dec = codecs(INITPYC.format(
        _init, 
        _rot_code,
        _s,
        _getattr, 
        _import, 
        chr_str('gzip'), 
        chr_str('decompress'), 
        _add,
        _getattr,
        _bytes,
        chr_str('fromhex'),
        _getattr,
        _globals,
        chr_str('pop'),
        chr_str(_enc_code_func),
        _getattr,
        _globals, 
        chr_str('pop'),
        chr_str(_pyc), 
        _f,
        chr_str(KEY[0], d=True), 
        _r,
        _getattr,
        _import,
        chr_str('io'),
        chr_str('BytesIO'),
        _getattr,
        _exec,
        chr_str('__getattribute__'),
        chr_str('__call__'),
        _rot,
        _for.tobytes(),
        _marshal,
        _getattr,
        _import,
        chr_str('__call__'),
        chr_str('marshal'),
        _getattr,
        _globals,
        chr_str('pop'),
        chr_str(_filter_bytes),
        _getattr,
        _globals,
        chr_str('pop'),
        chr_str(_filter),
        _getattr,
        _globals,
        chr_str('update'),
        chr_str(_code),
        _getattr,
        _marshal,
        chr_str('dumps'),
        _compile, 
        _getattr,
        _r,
        chr_str('getbuffer'),
        chr_str('<...>'), 
        chr_str('exec'),
        chr_str(0, d=True),
        choice(TRUE),
        _getattr,
        _marshal,
        chr_str('loads'),
        _eq,
        _getattr,
        _globals,
        chr_str('get'),
        chr_str('__name__'),
        chr_str('__main__'),
        _is,
        _debug,
        choice(NONE),
        _is,
        _getattr,
        _globals,
        chr_str('get'),
        chr_str('_'),
        choice(ELLIPSIS),
        _exec,
        _init,
        _getattr,
        _globals,
        chr_str('pop'),
        chr_str(_code),
        f'{{_:__ for(_,__)in({_getattr}({_getattr}({_globals}(),{chr_str("__getattribute__")})({chr_str("items")}),{chr_str("__getattribute__")})({chr_str("__call__")})())if(({_getattr}(_,{chr_str("startswith")})({chr_str("__")}))and({_getattr}(_,{chr_str("startswith")})({chr_str("__")})))}}',
        _exit,
        chr_str(0, d=True),
        _pyc
    ).encode(ENCODING), 'uu')


    payload = (
        f'{_getattr}({_getattr}({_getattr}({_globals},{chr_str("__call__")})(),{chr_str("__setitem__")}),{chr_str("__call__")})({chr_str(_pyc)},{_enc_code_body}),'
        f'{_exec}({_getattr}({_import}({chr_str("codecs")}),{chr_str("decode")})({_dec},{chr_str("uu")})),'
        '_start(main)'
    ).encode(ENCODING)


    packed_2 = lzma(
        payload,
        format=FORMAT_RAW,
        filters=LZMA_FILTER
    )


    _start.__reduce__ = lambda _: (main, (_module,))
    _main = f'__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("globals")}),{chr_str("__getattribute__")})({chr_str("__call__")})(),{chr_str("__getattribute__")})({chr_str("__setitem__")}),{chr_str("__getattribute__")})({chr_str("__call__")})({chr_str("main")},__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("__getattribute__")}),{chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("...")},(__builtins__.getattr(__builtins__,{chr_str("object")}),),{{{chr_str("__slots__")}:(),{chr_str("__or__")}:lambda _,__:lambda:(__builtins__.getattr(__,{chr_str("__getitem__")})({chr_str(1, d=True)})(__builtins__.getattr(__,{chr_str("__getitem__")})({chr_str(0, d=True)}))and(((({choice(NONE)})or({choice(NONE)})is({choice(NONE)})=={choice(TRUE)})))),{chr_str("__init__")}:lambda __,_:(__builtins__.getattr(__builtins__,{chr_str("exec")})(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("__import__")})({chr_str("base64")}),{chr_str("b85decode")})(_),__builtins__.getattr(__builtins__,{chr_str("globals")})()))if(_!=\'_\')else((({choice(ELLIPSIS)})!={choice(TRUE)})and({choice(NONE)}))}}))'.encode(ENCODING).hex()
    

    __start           = memoryview(pickle(_start()))
    _pickle_signature = __start[:24].hex()
    _pickled_body     = __start[24:].tobytes()


    packed_1 = zlib((
        f'__builtins__.setattr({_chr_func},{_chr_str(None, "__code__")},__builtins__.getattr(__builtins__.getattr({_chr_func},{_chr_str(None, "__code__")}),{_chr_str(None, "replace")})(**{{{_chr_str(None, "co_consts")}:__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr({_chr_func},{_chr_str(None, "__getattribute__")})({_chr_str(None, "__code__")}),{_chr_str(None, "co_consts")}),{_chr_str(None, "__getitem__")})(__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "slice")}),{_chr_str(None, "__new__")})(__builtins__.getattr(__builtins__,{_chr_str(None, "slice")}),({choice(NONE)})or({choice(NONE)}),~((((((~(~0<<1))<<3)>>2)|(((~(~0<<2))>>1)&(~0>>31)))^(((~(~0<<5))>>4)|((~(~0<<3))>>2)))>>1))),{_chr_str(None, "__add__")})(({chr_str(CHR_KEY[1], d=True)},{chr_str(CHR_KEY[0], d=True)}))}})),' 
        f'__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("exec")}),{chr_str("__getattribute__")}),{chr_str("__call__")})({chr_str("__call__")})(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("bytes")}),{chr_str("__getattribute__")}),{chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("bytes")})(),{chr_str("__new__")}),{chr_str("__getattribute__")})({chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("bytes")}),__builtins__.getattr(({choice(TRUE)})is({choice(TRUE)})==({choice(TRUE)}),{chr_str("to_bytes")})()),{chr_str("fromhex")})(\'{_main}\')),'
        f'__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("__getattribute__")}),{chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("type")}),{chr_str("...")},(__builtins__.getattr(__builtins__,{chr_str("object")}),),{{{chr_str("__slots__")}:(),{chr_str("__lshift__")}:lambda __,_:__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("memoryview")}),{chr_str("__new__")}),{chr_str("__getattribute__")})({chr_str("__call__")})(__builtins__.getattr(__builtins__,{chr_str("memoryview")}),__builtins__.getattr(__builtins__.getattr((({choice(TRUE)})==({choice(ELLIPSIS)})and({choice(NONE)})is({choice(NONE)})),{chr_str("to_bytes")})(),{chr_str("fromhex")})(\'{_pickle_signature}\')+_),{chr_str("__call__")}:lambda _:lambda:_&_,{chr_str(_pickled_code)}:__builtins__.getattr(__builtins__,{chr_str("memoryview")})({_pickled_body}),{chr_str("__and__")}:lambda __,_:__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{chr_str("globals")}),{chr_str("__call__")})(),{chr_str("__getattribute__")}),{chr_str("__call__")})({chr_str("__getitem__")})({chr_str("main")})(({chr_str("_")}))|(_<<__builtins__.getattr(__,{chr_str(_pickled_code)}),__builtins__.getattr(__,{chr_str(_loads)})),{chr_str(_loads)}:__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(getattr(__builtins__,{chr_str("globals")})(),{chr_str("get")})({chr_str("__builtins__")}),{chr_str("__import__")})({chr_str("pickle")}),{chr_str("loads")}),{chr_str("__init__")}:lambda _:(_()()())or(({choice(ELLIPSIS)})and({choice(TRUE)})and({choice(NONE)}))}})(),'
        f'{_exec}({_lzma}({packed_2}))\n'
        'if(__name__==\'__main__\'):main()'
    ).encode(ENCODING), wbits=-15, level=9)


    _char = f'lambda _:__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "str")})(),{_chr_str(None, "__getattribute__")})({_chr_str(None, "join")})([__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "chr")}),{_chr_str(None, "__getattribute__")})({_chr_str(None, "__call__")})((__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "ord")}),{_chr_str(None, "__getattribute__")})({_chr_str(None, "__call__")})(__)^True)>>False)for(__)in(_)])'


    packed_0 = (
        f'__builtins__.getattr(__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "type")}),{_chr_str(None, "__getattribute__")})(__builtins__.getattr(__builtins__,{_chr_str(None, "type")}),{_chr_str(None, "__new__")})(__builtins__.getattr(__builtins__,{_chr_str(None, "type")}),{_chr_str(None, "...")},(__builtins__.getattr(__builtins__,{_chr_str(None, "object")}),),{{'
        f'{_chr_str(None, "__slots__")}:(),'
        f'{_chr_str(None, "__or__")}:lambda __,_:__builtins__.getattr(__builtins__,{_chr_str(None, "exec")})(_,__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "globals")}),{_chr_str(None, "__getattribute__")})({_chr_str(None, "__call__")})()),'
        f'{_chr_str(None, "__add__")}:lambda _,__:__builtins__.getattr(__builtins__,{_chr_str(None, "eval")})("{_char}"),'
        f'{_chr_str(None, "__floordiv__")}:lambda _,__:__builtins__.getattr(__builtins__,{_chr_str(None, "__import__")})({_chr_str(None, "zlib")}),'
        f'{_chr_str(None, "__rshift__")}:lambda __,_:__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "globals")})(),{_chr_str(None, "__setitem__")})({_chr_str(None, "_")},{choice(ELLIPSIS)}),'
        f'{_chr_str(None, "__lshift__")}:lambda _,__:__builtins__.getattr(__builtins__.getattr(__builtins__,{_chr_str(None, "globals")})(),{_chr_str(None, "__setitem__")})({_chr_str(None, _chr_func)},({choice(NONE)})or(_)+({choice(NONE)})),'
        f'{_chr_str(None, "__init__")}:lambda __,_:(__<<__)or({choice(TRUE)})and(__>>__)or(__|__builtins__.getattr(__builtins__,{_chr_str(None, "compile")})(__builtins__.getattr((__//0),{_chr_str(None, "decompress")})(_,({choice(ELLIPSIS)})and({_chr_str(None, -15, d=True)})or({choice(NONE)})),{_chr_str(None, "<...>")},{_chr_str(None, "exec")},666%3,{choice(TRUE)}))and(({choice(NONE)})and({choice(NONE)}))'
        f'}}),{_chr_str(None, "__call__")})({packed_1})' 
    )


    with open(oname, 'w', encoding=ENCODING) as f:
        f.write(packed_0)
        f.flush()

    print(f'packed ({p}) created ({oname}) [+]')
    



def pypacker():
    if len(argv) < 2: 
        print(f'Usage: python{version_info.major} {splitp(__file__)[-1]} <pyfile>  —  Pack Python file')
        return


    for fp in argv[1:]: 
        if not isfile(fp):
            print(f'({fp}) is not file [*]')
            continue

        try:
            pypack(fp)
        except KeyboardInterrupt:
            return
        except Exception as er:
            print(f'unpacked ({fp}) [-]\n\n{type(er).__name__}({er})\n')




if __name__ == '__main__': pypacker()
