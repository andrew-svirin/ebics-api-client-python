import requests

class EbicsApiClient:

    def __init__(
        self,
        apiKey: str,
        apiHost: str
    ) -> None:
        self.apiKey = apiKey
        self.apiHost = apiHost

    def _make_request(self, method, endpoint, **kwargs):
        """
        Internal method for making requests
        """

        url = f"{self.apiHost}{endpoint}"

        headers = {
            'Accept': 'application/json',
            'Authorization': 'Key ' + self.apiKey,
        }

        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "body": e.response.text}

    # Connection Group.
    def connection_create(self, data):
        """
        Create connection.
        """
        return self._make_request('POST', '/api/ebics/connections/create', data=data)

    def connection_update(self, id, data):
        """
        Update connection.
        """
        return self._make_request('POST', '/api/ebics/connections/' + id + '/update', data=data)

    def connection_get(self, id):
        """
        Get connection.
        """
        return self._make_request('GET', '/api/ebics/connections/' + id)

    def connection_list(self):
        """
        List connections.
        """
        return self._make_request('GET', '/api/ebics/connections')

    def connection_delete(self, id):
        """
        Delete connection.
        """
        return self._make_request('DELETE', '/api/ebics/connections/' + id)

    # Keyring Group.
    def keyring_generate(self, data):
        """
        Generate keyring.
        """
        return self._make_request('POST', '/api/ebics/keyring/generate', data=data)

    def keyring_init(self, data):
        """
        Initialize keyring activation.
        """
        return self._make_request('POST', '/api/ebics/keyring/init', data=data)

    def keyring_suspend(self, data):
        """
        Suspend keyring activation.
        """
        return self._make_request('POST', '/api/ebics/keyring/suspend', data=data)

    def keyring_letter(self, data):
        """
        Get letter for keyring.
        """
        return self._make_request('POST', '/api/ebics/keyring/letter', data=data)

    def keyring_change_secret(self, data):
        """
        Change secret for keyring.
        """
        return self._make_request('POST', '/api/ebics/keyring/change-secret', data=data)

    # OrderType Group.
    def order_type_hev(self, data):
        """
        HEV Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/hev', data=data)

    def order_type_ini(self, data):
        """
        INI Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/ini', data=data)

    def order_type_hia(self, data):
        """
        HIA Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/hia', data=data)

    def order_type_hpb(self, data):
        """
        HPB Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/hpb', data=data)

    def order_type_hpd(self, data):
        """
        HPD Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/hpd', data=data)

    def order_type_hkd(self, data):
        """
        HKD Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/hkd', data=data)

    def order_type_htd(self, data):
        """
        HTD Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/htd', data=data)

    def order_type_haa(self, data):
        """
        HAA Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/haa', data=data)

    def order_type_fdl(self, data):
        """
        FDL Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/fdl', data=data)

    def order_type_ful(self, data):
        """
        FUL Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/ful', data=data)

    def order_type_ptk(self, data):
        """
        PTK Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/ptk', data=data)

    def order_type_vmk(self, data):
        """
        VMK Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/vmk', data=data)

    def order_type_sta(self, data):
        """
        STA Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/sta', data=data)

    def order_type_c52(self, data):
        """
        C52 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/c52', data=data)

    def order_type_c53(self, data):
        """
        C53 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/c53', data=data)

    def order_type_c54(self, data):
        """
        C54 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/c54', data=data)

    def order_type_z52(self, data):
        """
        Z52 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/z52', data=data)

    def order_type_z53(self, data):
        """
        Z53 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/z53', data=data)

    def order_type_z54(self, data):
        """
        Z54 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/z54', data=data)

    def order_type_zsr(self, data):
        """
        ZSR Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/zsr', data=data)

    def order_type_xek(self, data):
        """
        XEK Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/xek', data=data)

    def order_type_cct(self, data):
        """
        CCT Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/cct', data=data)

    def order_type_cip(self, data):
        """
        CIP Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/cip', data=data)

    def order_type_xe2(self, data):
        """
        XE2 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/xe2', data=data)

    def order_type_xe3(self, data):
        """
        XE3 Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/xe3', data=data)

    def order_type_yct(self, data):
        """
        YCT Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/yct', data=data)

    def order_type_cdb(self, data):
        """
        CDB Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/cdb', data=data)

    def order_type_cdd(self, data):
        """
        CDD Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/cdd', data=data)

    def order_type_btd(self, data):
        """
        BTD Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/btd', data=data)

    def order_type_btu(self, data):
        """
        BTU Order type.
        """
        return self._make_request('POST', '/api/ebics/order-types/btu', data=data)

    # AccessLog group.
    def access_log_list(self):
        """
        List AccessLogs.
        """
        return self._make_request('GET', '/api/ebics/logs')

    # FetchedFile group.
    def fetched_file_list(self):
        """
        List FetchedFiles.
        """
        return self._make_request('GET', '/api/ebics/fetched-files')

    def fetched_file_download(self, id):
        """
        Download FetchedFile.
        """
        return self._make_request('GET', '/api/ebics/fetched-files/' + id + '/download')