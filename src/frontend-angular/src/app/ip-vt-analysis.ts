export interface IpVtAnalysis {
  blocked?: boolean;
  ip: string;
  malicious: string;
  suspicious: string;
  harmless: string;
  lastModificationDate: string;
}
