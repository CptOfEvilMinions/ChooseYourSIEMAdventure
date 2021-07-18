class SIEM:
  def __init__(self, host, logFile):
    self.Host = host
    self.LogFile = logFile

class SplunkSIEM(SIEM):
  def __init__(self, host, logFile, ingestPort, index, sourceType, apiPort, siemUsername, siemPassword):
    self.Host = host
    self.Port = apiPort
    self.Index = index
    self.SourceType = sourceType
    self.LogFile = logFile
    self.SessionKey = str()
    self.IngestPort = ingestPort
    self.SiemUsername = siemUsername
    self.SiemPassword = siemPassword


class GraylogSIEM(SIEM):
  def __init__(self, host, logFile, ingestPort, index, sourceType, apiPort, siemUsername, siemPassword):
    self.Host = host
    self.Port = apiPort
    self.Index = index
    self.LogFile = logFile
    self.SessionKey = str()
    self.IngestPort = ingestPort
    self.SiemUsername = siemUsername
    self.SiemPassword = siemPassword

class LogstashSIEM(SIEM):
  def __init__(self, host, logFile, ingestPort):
    self.Host = host
    self.LogFile = logFile
    self.IngestPort = ingestPort


class ElasticsearchSIEM(SIEM):
  def __init__(self, host, logFile, ingestPort, index, threads, siemUsername=None, siemPassword=None):
    self.Host = host
    self.Index = index
    self.Threads = threads
    self.LogFile = logFile
    self.IngestPort = ingestPort
    self.SiemUsername = siemUsername
    self.SiemPassword = siemPassword
