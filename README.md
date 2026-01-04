# Server-Unifi-Log

## UniFi Controller Data Monitoring and Logging

This repository contains a Python script designed to interact with a **UniFi Controller** and periodically log detailed information about the network status, devices, clients, and events. It is an essential tool for network administrators looking to automate the collection of log data and monitor the health of their UniFi environment.

---

## 🌟 Key Features

The `Server_Unifi_Log.py` script runs a monitoring cycle every 15 seconds, collecting and logging the following information:

*   **Device Inventory**: Logs all UniFi devices (APs, Switches, Gateways) with details such as name, model, IP address, MAC, uptime, and firmware version.
*   **Network Health**: Aggregated health data for the UniFi network.
*   **Network Configuration**: Detailed information about the network configurations defined in the controller.
*   **Rogue Access Points**: A list of unauthorized Access Points (APs) detected within the last 24 hours.
*   **Server Status**: Status statistics for the UniFi controller server.
*   **Server Events**: Logs the last 720 hours (30 days) of controller events.
*   **WLAN Configuration**: Details of the wireless network (WLAN) configurations.

## ⚙️ Prerequisites

To run this script, you need the following components:

1.  **Python 3**: The script is developed in Python.
2.  **UniFi Controller**: Access to a running UniFi Controller (local or cloud-hosted).
3.  **Access Credentials**: A user with read permissions on the UniFi Controller.

## 🛠️ Installation

Follow the steps below to set up the execution environment:

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Pedro-Jorge18/Server-Unifi-Log.git
    cd Server-Unifi-Log
    ```

2.  **Install Dependencies**:
    The script uses the `unificontrol` library to communicate with the controller.
    ```bash
    pip install unificontrol
    ```

## 📝 Configuration

Edit the `Server-Unifi-Log/Server Unifi Log/Server_Unifi_Log.py` file to configure the access credentials for your UniFi Controller.

Locate lines 7 to 11 and replace the placeholder values (`....`, `.....`, `......`) with your controller's actual data:

```python
client = UnifiClient(
    host="<CONTROLLER_IP_OR_HOST>", # host of the controller
    username="<USERNAME>", # username of the controller
    password="<PASSWORD>", # password of the controller
)
```

## ▶️ Usage

After configuration, you can run the script as follows:

```bash
python "Server Unifi Log/Server_Unifi_Log.py"
```

The script will start monitoring and create a new log file in the execution directory every 15 seconds.

### Log File Format

Log files are created with the name `log_ubiquiti_YYYY-MM-DD`, where `YYYY-MM-DD` is the current date. The content is a mix of formatted text for devices and blocks of data in **JSON** format for network statistics.
