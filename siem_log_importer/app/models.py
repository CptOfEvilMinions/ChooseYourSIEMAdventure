class SIEM:
  def __init__(self, host, port, index, logFile, platform, ingest_port, siemUsername, siemPassword) -> None:
    self.Host = host
    self.Port = port
    self.Index = index
    self.LogFile = logFile
    self.Platform = platform
    self.SessionKey = None
    self.Ingest_port = ingest_port
    self.SiemUsername = siemUsername
    self.SiemPassword = siemPassword