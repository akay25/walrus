import request from "@/utils/request"

export function fetchVPNServers() {
  return request({
    url: "/vpn-servers",
    method: "get"
  })
}
