<data inherit_id="web.layout">
    <xpath expr="//body" position="inside">
        <t t-if="request.httprequest.cookies.get('cids') and request.httprequest.cookies.get('cids')[0] == '1'">
            <style>.o_main_navbar {background: linear-gradient(45deg, #57596F, #57596F);
                                   bacground-color: #57596F!important;border-botom: 0px;}</style></t>

        <t t-if="request.httprequest.cookies.get('cids') and request.httprequest.cookies.get('cids')[0] == '2'">
                    <style>.o_main_navbar {background: linear-gradient(45deg, #DA2325, #DA2325);
                                           bacground-color: #DA2325!important;border-botom: 0px;}</style></t>

        <t t-if="request.httprequest.cookies.get('cids') and request.httprequest.cookies.get('cids')[0] == '3'">
                    <style>.o_main_navbar {background: linear-gradient(45deg, #2DB446, #2DB446);
                                           bacground-color: #2DB446!important;border-botom: 0px;}</style></t>

        <t t-if="request.httprequest.cookies.get('cids') and request.httprequest.cookies.get('cids')[0] == '3'">
                    <style>.o_main_navbar {background: linear-gradient(45deg, #B945C4, #B945C4);
                                           bacground-color: #B945C4!important;border-botom: 0px;}</style></t>
    </xpath>
</data>