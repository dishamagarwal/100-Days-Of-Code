import requests
import json

ENDPOINT = "https://oldmatrix.itasoftware.com/search"
HEADERS = {
  'X-GWT-Permutation': 'blah',
  'Content-Type': 'application/javascript; charset=UTF-8',
}

class Scraper:
    def __init__(self, date, origin, dest, flnum):
        self.date = date
        self.origin = origin
        self.dest = dest
        self.flnum = flnum

    def _atoi_dict(self, d):
        if isinstance(d, dict):
            converted_dict = {}
            for key, value in d.items():
                converted_key = int(key) if key.isdigit() else key
                converted_value = self._atoi_dict(value)
                converted_dict[converted_key] = converted_value
            return converted_dict
        elif isinstance(d, list):
            return [self._atoi_dict(item) for item in d]
        elif isinstance(d, str):
            try:
                return int(d) if d.isdigit() else float(d)
            except ValueError:
                return d
        else:
            return d

    def _find_usd(self, d):
            if isinstance(d, dict):
                for key, value in d.items():
                    result = self._find_usd(value)
                    if result is not None:
                        return result
            elif isinstance(d, list):
                for item in d:
                    result = self._find_usd(item)
                    if result is not None:
                        return result
            elif isinstance(d, str) and d.startswith("USD"):
                try:
                    usd_value = float(d.lstrip("USD"))
                    return usd_value
                except ValueError:
                    pass
            return None
            
    def get_price(self):
        payload = f"{{\"method\":\"search\",\"params\":\"{{\\\"2\\\":[\\\"carrierStopMatrix\\\",\\\"currencyNotice\\\",\\\"durationSliderItinerary\\\",\\\"itineraryArrivalTimeRanges\\\",\\\"itineraryCarrierList\\\",\\\"itineraryDepartureTimeRanges\\\",\\\"itineraryDestinations\\\",\\\"itineraryOrigins\\\",\\\"itineraryPriceSlider\\\",\\\"itineraryStopCountList\\\",\\\"solutionList\\\",\\\"warningsItinerary\\\"],\\\"3\\\":{{\\\"4\\\":{{\\\"1\\\":1,\\\"2\\\":30}},\\\"5\\\":{{\\\"1\\\":1}},\\\"7\\\":[{{\\\"3\\\":[\\\"{self.dest}\\\"],\\\"5\\\":[\\\"{self.origin}\\\"],\\\"8\\\":\\\"{self.date}\\\",\\\"9\\\":0,\\\"11\\\":0,\\\"12\\\":\\\"{self.flnum}\\\"}}],\\\"8\\\":\\\"COACH\\\",\\\"9\\\":0,\\\"10\\\":1,\\\"15\\\":\\\"SUNDAY\\\",\\\"16\\\":0,\\\"17\\\":0,\\\"22\\\":\\\"default\\\",\\\"25\\\":0}},\\\"4\\\":\\\"specificDates\\\",\\\"7\\\":\\\"blah\\\",\\\"8\\\":\\\"wholeTrip\\\"}}\"}}"
        response = requests.request("POST", ENDPOINT, headers=HEADERS, data=payload)
        
        as_json = json.loads(response.text)

        processed_dict = self._atoi_dict(as_json)
        fare_usd = self._find_usd(processed_dict)
        
        return fare_usd