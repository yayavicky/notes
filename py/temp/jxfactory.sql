-- CREATE DATABASE IF NOT EXISTS jxfactory;
-- CREATE DATABASE IF NOT EXISTS jxfactory DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_chinese_ci;

DROP DATABASE jxfactory IF EXISTS;
CREATE DATABASE IF NOT EXISTS jxfactory DEFAULT CHARACTER SET utf8;

USE jxfactory;

 CREATE TABLE meteroutfactory(
    SN INT(20) not null primary key auto_increment,
    OrderNo VARCHAR(20) NULL,
    DeviceID VARCHAR(20) NOT NULL,
    OperatorUser VARCHAR(10) NULL,
    SceneType VARCHAR(20) NULL,
    Factory VARCHAR(10) NULL,
    ProjectDesc VARCHAR(100) NULL,
    Status VARCHAR(1) NOT NULL,
    PCBCode VARCHAR(20) NULL,
    StartDate datetime NOT NULL,
    EndDate datetime NOT NULL
 );

  CREATE TABLE meteroutfactorydetail(
    SN INT(20) not null primary key auto_increment,
    DeviceID VARCHAR(20) NOT NULL,
    SceneType VARCHAR(20) NULL,
    CmdNum INT(11) NOT NULL,
    CmdDescription VARCHAR(100) NULL,
    ScreenValue VARCHAR(100) NULL,    
    ActValue VARCHAR(100) NULL,    
    ResultValue VARCHAR(50) NULL,    
    ExecStatus VARCHAR(1) NOT NULL,
    ExecDate datetime NOT NULL
 );

