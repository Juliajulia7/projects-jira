from jira import JIRA
import time


class ForJira(object):

    def __init__(self, filter, login, password): #добавить login, pass
        self.filter = filter
        self.login = login
        self.password=password

    def authorization(self):
        jira_options = {'server': 'https://jira.'} #исправила адрес
        jira = JIRA(options=jira_options, basic_auth=(self.login, self.password))
        return jira

    def oneResult(self,instJira):
        pcrf_array_old = []
        filters=self.filter
        for k in filters:
            for i in instJira.search_issues(k, maxResults=5):
                str1 = i.fields.summary + i.permalink()
                pcrf_array_old.append(str1)
        return pcrf_array_old

    def getResult(self, pcrf_array_old, pcrf_array_new, instJira): #в осн.классе добавить pcrf_array_new и WHILE И time.sleep(60)
        filters = self.filter
        for k in filters:
            for i in instJira.search_issues(k, maxResults=7):
                str1=i.fields.summary+i.permalink()
                pcrf_array_new.append(str1)
        if(pcrf_array_new==pcrf_array_old):
            return [0, pcrf_array_old, pcrf_array_new]
        else:
            result=list(set(pcrf_array_new).difference(set(pcrf_array_old)))
            return [result, pcrf_array_old, pcrf_array_new]


# jira_server = {'server': jira_server}
# jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))

