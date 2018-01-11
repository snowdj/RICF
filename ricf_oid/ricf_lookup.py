# ricf_oid lookup module.
import pandas as pd
df_ricf_oid=pd.read_csv('https://raw.githubusercontent.com/ma-ji/RICF/master/ricf_oid/ricf_oid.tsv', sep='\t')
def ricf_lookup(ricf_oid=None, foundation_name=None, uscc=None):
    if foundation_name!=None and ricf_oid==None and uscc==None:
        df_ricf_oid_temp=df_ricf_oid.set_index('name_set')
        name_set_matched=[s for s in df_ricf_oid_temp.index if foundation_name in s.split('#')]
        if len(name_set_matched)==1:
            oid_uscc={'ricf_oid':df_ricf_oid_temp.loc[name_set_matched[0], 'ricf_oid'], 'nacao_uscc':df_ricf_oid_temp.loc[name_set_matched[0], 'nacao_uscc']}
        elif len(name_set_matched)==0:
            oid_uscc={'ricf_oid':'NotFound', 'nacao_uscc':'NotFound'}
        elif len(name_set_matched)>1:
            oid_uscc={'ricf_oid':'MoreThanOneMatch', 'nacao_uscc':'MoreThanOneMatch'}
        return oid_uscc
    elif foundation_name==None and ricf_oid!=None and uscc==None:
        ricf_oid=int(ricf_oid)
        df_ricf_oid_temp=df_ricf_oid.set_index('ricf_oid')
        if ricf_oid in df_ricf_oid_temp.index:
            name_uscc={'ba_cn':df_ricf_oid_temp.loc[ricf_oid, 'ba_cn'], 'nacao_uscc':df_ricf_oid_temp.loc[ricf_oid, 'nacao_uscc']}
        else:
            name_uscc={'ba_cn':'NotFound', 'nacao_uscc':'NotFound'}
        return name_uscc
    elif foundation_name==None and ricf_oid==None and uscc!=None:
        uscc=str(uscc)
        df_ricf_oid_temp=df_ricf_oid.set_index('nacao_uscc')
        if uscc in df_ricf_oid_temp.index:
            name_oid={'ba_cn':df_ricf_oid_temp.loc[uscc, 'ba_cn'], 'ricf_oid':df_ricf_oid_temp.loc[uscc, 'ricf_oid']}
        else:
            name_oid={'ba_cn':'NotFound', 'ricf_oid':'NotFound'}
        return name_oid
    elif len(set([s for s in (ricf_oid, foundation_name, uscc) if s!=None])) >1:
        raise NameError("Only need one parameter (ricf_oid/foundation_name/uscc).")
    elif len(set([s for s in (ricf_oid, foundation_name, uscc) if s!=None])) <1:
        raise NameError("Need at least one parameter (ricf_oid/foundation_name/uscc).")