#ifndef PROJECT_CONFIGURATION_H_
#define PROJECT_CONFIGURATION_H_

class Configuration {
public:
    String callsign;
    class Network {
    public:
        bool DHCP;
        class Static {
        public:
            IPAddress ip;
            IPAddress subnet;
            IPAddress gateway;
            IPAddress dns1;
            IPAddress dns2;
        };
        class Hostname {
        public:
            bool overwrite;
            String name;
        };
    };
    class Wifi {
    public:
        bool active;
    };
};

#endif
